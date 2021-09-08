#!/usr/bin/env python3
import rospy
import actionlib
from actionlib import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class MoveController:
    def __init__(self):
        self.ros_msg_client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        self.ros_msg_client.wait_for_server()

    def goal_pose(self, pose):
        goal_pose = MoveBaseGoal()
        goal_pose.target_pose.header.frame_id = "map"
        goal_pose.target_pose.header.stamp = rospy.Time.now()
        goal_pose.target_pose.pose.position.x = pose[0][0]
        goal_pose.target_pose.pose.position.y = pose[0][1]
        goal_pose.target_pose.pose.position.z = pose[0][2]
        goal_pose.target_pose.pose.orientation.x = pose[1][0]
        goal_pose.target_pose.pose.orientation.y = pose[1][1]
        goal_pose.target_pose.pose.orientation.z = pose[1][2]
        goal_pose.target_pose.pose.orientation.w = pose[1][3]

        return goal_pose

    def move_to_goal(self, pose: list, duration: int = 60):
        goal = self.goal_pose(pose)
        self.ros_msg_client.send_goal(goal)
        self.ros_msg_client.wait_for_result(rospy.Duration(duration))

    def move_goods_zone(self, pose, duration=60):
        rospy.loginfo("Go to Move Goods Zone")
        self.move_to_goal(pose, duration)

        if self.ros_msg_client.get_state() ==  GoalStatus.SUCCEEDED:
            rospy.loginfo("LOTTI is arrived in goodsZone")
            return True
        else:
            rospy.loginfo("LOTTI is not arrived in goodsZone")
            return False

    def move_load_zone(self, pose, duration=60):
        rospy.loginfo("Go to Load Zone")
        self.move_to_goal(pose, duration)

        if self.ros_msg_client.get_state() ==  GoalStatus.SUCCEEDED:
            rospy.loginfo("LOTTI is arrived in LoadZone")
            return True
        else:
            rospy.loginfo("LOTTI is not arrived in LoadZone")
            return False

    def move_wait_zone(self, pose, duration=60):
        rospy.loginfo("Go to Wait Zone")
        self.move_to_goal(pose, duration)

        if self.ros_msg_client.get_state() ==  GoalStatus.SUCCEEDED:
            rospy.loginfo("LOTTI is arrived in WaitZone")
            return True
        else:
            rospy.loginfo("LOTTI is not arrived in WaitZone")
            return False

if __name__ == "__main__":
    rospy.init_node("test_move_control")

    controller = MoveController()

    ## robot goods zone success test
    # result = controller.move_goods_zone([(2.1, 2.2, 0.0), (0.0, 0.0, 0.0, 1.0)], 59)
    # rospy.loginfo("Test Success") if result else rospy.loginfo("Test Fail")

    ## robot goods zone fail test
    # Set self.ros_msg_client.wait_for_reuslt(rospy.Duration(3)) in the move_* method
    result = controller.move_goods_zone([(0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 1.0)], 9)
    rospy.loginfo("Test Success") if not result else rospy.loginfo("Test Fail")

    rospy.spin()