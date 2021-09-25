#!/usr/bin/env python3
from logging import error
from rospy.core import rospyinfo
from state import StateManager
from move_control import MoveController
from way_points_manager import WayPointsManager
from load import Loader
from recognize import Recognizer
from std_msgs.msg import String
from lotti_nav.srv import WhereIgo
import rospy
import heapq

class Lotti:
    def __init__(self):
        self.zone_manager = WayPointsManager()
        self.move_controller = MoveController()
        self.recognizer = Recognizer()
        self.loader = Loader(move_controller=self.move_controller, recognizer=self.recognizer)
        self.state = StateManager.Wait
        self.destination = None
        self.first_operate = True
        self.lifting = False
        self.target_product = None
        self.priority = {"red": 0, "green": 1, "blue": 2}
        self.priority_q = []

    def request_destination(self, request, timeout=10):
        try:
            rospy.loginfo("Checking Service Server ...")
            rospy.wait_for_service("Where_I_go", timeout=timeout)
            rospy.loginfo("Success Checking Service Server !")
            des_requester = rospy.ServiceProxy("Where_I_go", WhereIgo)
            rospy.loginfo(f"Lotti request destination Where I go ? : {request}")
            destination = des_requester(request).destination
            rospy.loginfo(f"Lotti was Recevied destination {destination}")
        except rospy.ServiceException as e:
            rospy.loginfo(f"Error : {e}")
            destination = None

        return destination

    def operate_wait_case(self, wait_zone: str = "wait_zone1"):
        rospy.loginfo(f"Lotti State is {self.state}")
        if self.first_operate:
            self.first_operate = False
            pass
        else:
            self.destination = self.request_destination('ready')

        if self.destination is None:
            pose = self.zone_manager.get_wait_pose(wait_zone)
            _ = self.move_controller.move_wait_zone(pose)
        else:
            self.state = StateManager.Drive
    
    def operate_drive_case(self):
        rospy.loginfo(f"Lotti State is {self.state}")
        rospy.loginfo(f"Destination is : {self.destination}")
        pose = self.zone_manager.get_goods_pose(self.destination)
        ret = self.move_controller.move_goods_zone(pose)
        if ret:
            self.state = StateManager.Recognition
            rospy.loginfo("Changing State Drive to Recognition")
            self.destination = None
        else:
            self.state = StateManager.Wait

    def operate_recognition_case(self):
        import os
        rospy.loginfo("Recognition State")
        rospy.sleep(2)
        pub_dict = {"middle": 0, "right": 2, "left": 1}
        topic_name = "which_launch"
        os.system(f"rostopic pub -1 {topic_name} std_msgs/Int32 {pub_dict['middle']}")
        rospy.sleep(5)
        bbox_dict = self.recognizer.get_bbox_info(width_thr=195)
        while len(bbox_dict.keys()) < 1:
            self.move_controller.go_with_vel(linear_vel=[0.55, 0., 0.])
            rospy.sleep(5)
            bbox_dict = self.recognizer.get_bbox_info(width_thr=195)

        self.move_controller.go_with_vel()
        for key, value in bbox_dict.items():
            rospy.loginfo(f"Got ... Product : {key}, bbox : {value}\n")
            if key != "rolltainer":
                for _, xmin, _, xmax, _ in value:
                    location = self.recognizer.is_left_right(center=(self.recognizer.img_w_h[0]//2, 0),
                                                             current=(xmin + (xmax - xmin)//2, 0), error_bound=70.)
                    heapq.heappush(self.priority_q, (self.priority[key], key, location))
        
        self.state = StateManager.Load
        rospy.loginfo("Changing State Recognition to Load")

    def operate_load_case(self):
        rospy.loginfo("Load State")
        
        _, self.target_product_name, location = heapq.heappop(self.priority_q)
        self.destination = self.request_destination(self.target_product_name)

        while self.destination is None:
            if self.priority_q == []:
                self.state = StateManager.Wait
                return

            _, self.target_product_name, location = heapq.heappop(self.priority_q)
            self.destination = self.request_destination(self.target_product_name)
        
        rospy.loginfo(f"{self.target_product_name}'s destination : {self.destination}")
        self.priority_q = []

        direction = "middle"
        if location:
            direction = "left"
        elif location is None:
            direction = "middle"
        else:
            direction = "right"

        self.loader.enter_rolltainer(target_product_name=self.target_product_name, direction=direction)
        _ = self.loader.lift_up_down(target_pos=4.0, timeout=10.)
        self.loader.escape_rolltainer()
        
        pose = self.zone_manager.get_load_pose(self.destination)
        ret = self.move_controller.move_load_zone(pose)
        self.destination = None

        while not ret:
            ret = self.move_controller.move_load_zone(pose)

        self.loader.lift_up_down(target_pos=0.0, timeout=10.)
        rospy.sleep(2)
        self.loader.escape_rolltainer()
        self.state = StateManager.Wait
        rospy.loginfo("Success Getting Off")
        rospy.loginfo("Changing ... State Load to Wait")

    def operate(self):
        while True:
            # Wait State
            if self.state == StateManager.Wait:
                self.operate_wait_case()
            
            # Drive State
            elif self.state == StateManager.Drive:
                self.operate_drive_case()

            # Recognition State
            elif self.state == StateManager.Recognition:
                self.operate_recognition_case()

            # Load State
            elif self.state == StateManager.Load:
                self.operate_load_case()

            else:
                break
        

if __name__ == "__main__":
    rospy.init_node("LOTTI")
    rospy.loginfo("Test Start")

    lotti = Lotti()
    lotti.operate()

    rospy.spin()
                
