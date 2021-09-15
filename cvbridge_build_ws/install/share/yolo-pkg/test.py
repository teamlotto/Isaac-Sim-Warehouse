#!/usr/bin/env python3
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import rospy
import cv2
import numpy as np
import time
import os

class ImageProcessor:
    def __init__(self, save_path, is_show=False, is_save=False):
        self.img_sub = rospy.Subscriber("rgb", Image, self.sub_image)
        self.bridge = CvBridge()
        self.is_show = is_show
        self.is_save = is_save
        self.save_path = save_path

    def load_image(self, load_path):
        pass

    def save_image(self, image, save_path):
        image = np.array(image)
        path = os.path.join(save_path, str(int(time.time() * 1000)) + ".png")
        rospy.loginfo(f"save : {path}")
        rospy.loginfo(f"img type : {type(image)}, {image.shape}")
        cv2.imwrite(path, image)
        

    def show_image(self, image):
        cv2.imshow("image", image)
        cv2.waitKey(1)

    def pub_image(self):
        pass

    def sub_image(self, msg):
        rospy.loginfo(f"sub!")
        origin = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        if self.is_show:
            self.show_image(origin)
        if self.is_save:
            self.save_image(origin, self.save_path)

if __name__ == "__main__":
    import sys
    rospy.init_node("ImageProcess")

    rospy.Rate(10)
    save_path = "/root/job_in_docker/imgs/test"
    processor = ImageProcessor(is_show=True, is_save=True, save_path=save_path)
    # import numpy as np
    # import os
    # a = np.array([[0]*100])
    # path = os.path.join(save_path, "test2.png")
    # rospy.loginfo(path)
    # cv2.imwrite(path, a)

    rospy.spin()
