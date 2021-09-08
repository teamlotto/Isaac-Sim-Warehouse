import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

class MoveController():
    def __init__(self):
        self.ros_msg_client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        self.ros_msg_client.wait_for_server()

    def goal_pose(pose):
        goal_pose = MoveBaseGoal()
        goal_pose.target_pose.header.frame_id = "map"
        goal_pose.target_pose.pose.position.x = pose[0][0]
        goal_pose.target_pose.pose.position.y = pose[0][1]
        goal_pose.target_pose.pose.position.z = pose[0][2]
        goal_pose.target_pose.pose.orientation.x = pose[1][0]
        goal_pose.target_pose.pose.orientation.y = pose[1][1]
        goal_pose.target_pose.pose.orientation.z = pose[1][2]
        goal_pose.target_pose.pose.orientation.w = pose[1][3]

        return goal_pose

    def move_goods_zone(self, pose):
        goal = self.goal_pose(pose)
        self.ros_msg_client.send_goal(pose)
        self.ros_msg_client.wait_for_result()

        if self.ros_msg_client.get_state() ==  GoalStatus.SUCCEEDED:
            return True
        else:
            return False

    def move_load_zone(self, pose):
        pass

    def move_wait_zone(self, pose):
        pass