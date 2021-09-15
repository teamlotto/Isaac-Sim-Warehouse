#!/usr/bin/env python3

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

class ImageProcessor:
    def __init__(self):
        self.img_sub = rospy.Subscriber("rgb", Image, self.sub_image)
        self.bridge = CvBridge()

    def load_image(self, load_path):
        pass

    def save_image(self, save_path):
        pass

    def show_image(self, image):
        cv2.imshow("image", image)
        cv2.waitKey(1)

    def pub_image(self):
        pass

    def sub_image(self, msg):
        rospy.loginfo(f"sub!")
        origin = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        # self.show_image(origin)

if __name__ == "__main__":
    rospy.init_node("ImageProcess")
    processor = ImageProcessor()
    rospy.spin()


