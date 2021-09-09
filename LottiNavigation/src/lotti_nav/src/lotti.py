#!/usr/bin/env python3
from rospy.core import rospyinfo
from state import StateManager
from move_control import MoveController
from way_points_manager import WayPointsManager
from std_msgs.msg import String
import rospy

class Lotti:
    def __init__(self):
        self.zone_manager = WayPointsManager()
        self.move_controller = MoveController()
        self.state = StateManager.Wait
        self.destination = None

    def request_destination(self, timeout=None):
        def dest_callback(msg):
            self.destination = msg.data
        pub = rospy.Publisher('where', String, queue_size=1)
        pub.publish("Where I go ?")
        sub = rospy.Subscriber('where', String, callback=dest_callback)
        rospy.loginfo("Wait for destination")
        rospy.wait_for_message('where', String, timeout=timeout)

    def operate_wait_case(self, wait_zone: str = "wait_zone1"):
        pose = self.zone_manager.get_wait_pose(wait_zone)
        ret = self.move_controller.move_wait_zone(pose)
        self.request_destination()

        if self.destination is not None:
            self.state = StateManager.Drive
    
    def operate_drive_case(self):
        rospy.loginfo(f"destination : {self.destination}")
        self.destination = 'goods_zone2' if self.destination is None else self.destination
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
        rospy.info("Load State")
        pose = self.zone_manager.get_load_pose('load_red')
        ret = self.move_controller.move_load_zone(pose)
        if ret:
            pose = self.zone_manager.get_wait_pose('wait_zone1')
            ret = self.move_controller.move_wait_zone(pose)
            if ret:
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
            # elif self.state == StateManager.Load:
                # rospy.info("Load State")
                # pose = self.zone_manager.get_load_pose('load_red')
                # ret = self.move_controller.move_load_zone(pose)
                # if ret:
                #     pose = self.zone_manager.get_wait_pose('wait_zone1')
                #     ret = self.move_controller.move_wait_zone(pose)
                #     if ret:
                #         self.state = StateManager.Wait
        

if __name__ == "__main__":
    rospy.init_node("LOTTI")
    rospy.loginfo("Test Start")

    lotti = Lotti()
    lotti.operate()

    rospy.spin()
                
