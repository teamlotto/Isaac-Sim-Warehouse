#!/usr/bin/env python3

import cv2
from sensor_msgs.msg import Image
import rospy
from cv_bridge import CvBridge

def callback(msg):
    img = bridge.imgmsg_to_cv2(msg)
    cv2.imshow("test", img)
    cv2.waitKey(1)
    cv2.cv2.destroyAllwindows()

rospy.init_node("test")

bridge = CvBridge()
sub = rospy.Subscriber('/rgb', Image, callback)
rospy.spin()
