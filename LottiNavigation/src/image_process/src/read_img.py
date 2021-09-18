#!/usr/bin/env python3

import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from darknet_ros_msgs.msg import BoundingBoxes
import cv2

def cbf(msg):
    img = bridge.imgmsg_to_cv2(msg)
    cv2.imshow("test", img)
    cv2.waitKey(1)
    cv2.destroyAllwindows()

def bbox(msg):
    rospy.loginfo(msg)

rospy.init_node("test_image")
sub = rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, callback=bbox)

bridge = CvBridge()

rospy.spin()