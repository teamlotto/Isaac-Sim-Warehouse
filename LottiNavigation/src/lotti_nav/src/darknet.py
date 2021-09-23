#!/usr/bin/env python3

import rospy
from rospy.topics import Subscriber
from std_msgs.msg import Int32
import os

def launch_darknet(msg):
    rospy.loginfo(msg.data)
    rospy.loginfo(msg.data == 1)
    rospy.loginfo(type(msg))

    if msg.data == 0:
        os.system("roslaunch darknet_ros yolo_v4_tiny_rolltainer.launch")
        rospy.sleep(6)
    elif msg.data == 1:
        os.system("roslaunch darknet_ros yolo_v4_tiny_rolltainer_right.launch")
        rospy.sleep(6)
    elif msg.data == 2:
        os.system("roslaunch darknet_ros yolo_v4_tiny_rolltainer_left.launch")
        rospy.sleep(6)
    else:
        rospy.loginfo(f"Unkown data : {msg.data}")

if __name__ == "__main__":
    rospy.init_node('darknet_starter')
    rospy.loginfo("darknet ros node wating start")
    rospy.Rate(2)

    sub = rospy.Subscriber("which_launch", Int32, launch_darknet)
    rospy.spin()