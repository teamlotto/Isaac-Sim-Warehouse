#!/usr/bin/env python3
from logging import error
from rospy.core import rospyinfo
from state import StateManager
from move_control import MoveController
from way_points_manager import WayPointsManager
from load import Loader
from std_msgs.msg import String
from lotti_nav.srv import WhereIgo
import rospy

class Lotti:
    def __init__(self):
        self.zone_manager = WayPointsManager()
        self.move_controller = MoveController()
        self.loader = Loader()
        self.state = StateManager.Wait
        self.destination = None
        self.first_operate = True

    def request_destination(self, request, timeout=10):
        try:
            rospy.loginfo("Checking Service Server ...")
            rospy.wait_for_service("Where_I_go", timeout=timeout)
            rospy.loginfo("Success Checking Service Server !")
            des_requester = rospy.ServiceProxy("Where_I_go", WhereIgo)
            rospy.loginfo(f"Lotti request destination Where I go ?")
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
            self.destination = self.request_destination(1)

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
        rospy.loginfo("Recognition State")
        self.state = StateManager.Load
        rospy.loginfo("Changing State Recognition to Load")

    def operate_load_case(self):
        rospy.loginfo("Load State")
        self.loader.lift_up_down(target_pos=4.0, timeout=10.)
        pose = self.zone_manager.get_load_pose('load_red')
        rospy.loginfo(f"pose {pose}")
        ret = self.move_controller.move_load_zone(pose)
        if ret:
            self.loader.lift_up_down(target_pos=0.0, timeout=10.)
            self.state = StateManager.Wait

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

            # # Load State
            elif self.state == StateManager.Load:
                self.operate_load_case()
        

if __name__ == "__main__":
    rospy.init_node("LOTTI")
    rospy.loginfo("Test Start")

    lotti = Lotti()
    lotti.operate()

    rospy.spin()
                
