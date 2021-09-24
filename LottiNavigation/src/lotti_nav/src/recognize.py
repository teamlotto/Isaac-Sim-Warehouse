#!/usr/bin/env python3
import rospy
from rospy.core import rospyinfo
from sensor_msgs.msg import LaserScan
from darknet_ros_msgs.msg import BoundingBoxes
from collections import defaultdict

class Recognizer():
    def __init__(self, img_w_h = (1280, 750)):
        self.img_w_h = img_w_h

    def get_bbox_info(self, width_thr:float = 10.) -> dict:
        msg = rospy.wait_for_message("/darknet_ros/bounding_boxes", BoundingBoxes, timeout=2)
        bbox_dict = defaultdict(list)
        [ bbox_dict[info.Class].append((round(info.probability, 3), info.xmin, info.ymin, info.xmax, info.ymax)) for info in msg.bounding_boxes
         if (info.xmax - info.xmin) > width_thr ]
        
        return bbox_dict

    def get_bbox_center(self, class_name: str, prb_thr: float = 0.9, width_thr: float = 50.) -> dict:
        bbox_dict = self.get_bbox_info()
        center_dict = {}
        pass_err = 0
        if class_name in bbox_dict.keys():
            bbox_dict[class_name].sort(key=lambda x: x[1])
            for idx, infos in enumerate(bbox_dict[class_name]):
                prb , xmin, ymin, xmax, ymax = infos
                if prb < prb_thr or (xmax - xmin) < width_thr:
                    pass_err += 1
                    continue
                center_dict[idx-pass_err] = (xmin + (xmax - xmin) // 2, ymin + (ymax - ymin) // 2)

        return center_dict

    def get_bbox_width(self, class_name: str, prb_thr: float = 0.9, width_thr: float = 50.) -> dict:
        bbox_dict = self.get_bbox_info()
        width_dict = {}
        pass_err = 0
        if class_name in bbox_dict.keys():
            bbox_dict[class_name].sort(key=lambda x: x[1])
            for idx, infos in enumerate(bbox_dict[class_name]):
                prb , xmin, _, xmax, _ = infos
                if prb < prb_thr or (xmax - xmin) < width_thr:
                    pass_err += 1
                    continue
                width_dict[idx-pass_err] = (xmax - xmin)

        return width_dict

    def match_image_center(self, center, img_wh: tuple = None, error_bound = 3):
        if img_wh is None:
            img_wh = self.img_w_h
        w, _ = img_wh
        rospy.loginfo(f"Matching center ... {w // 2 - error_bound} {center[0]} {w // 2 + error_bound}")
        if w // 2 - error_bound < center[0] < w // 2 + error_bound:
            return True
        else:
            return False

    def is_left_right(self, center, current, error_bound:int = 0):
        """
        center에서 오른쪽인지 왼쪽인지 알려주는 함수
        """
        rospy.loginfo(f"center : {center}, current : {current}, {center[0] - error_bound} < {current[0]} < {center[0] + error_bound}")
        if center[0] - error_bound > current[0]:
            rospy.loginfo(f"Left from the center")
            return True
        elif center[0] + error_bound < current[0]:
            rospy.loginfo(f"Right from the center")
            return False
        else:
            rospy.loginfo(f"Center or Error")
            return None

    def get_lidar_value(self, idxes:list = [], left_thr=0.3, right_thr=0.6) -> tuple:
        msg = rospy.wait_for_message("/scan", LaserScan, timeout=2)
        rospy.loginfo(f"Got ... range length : {len(msg.ranges)}")
        lidar_values = [ msg.ranges[idx] for idx in idxes ] if idxes else msg.ranges
        lidar_values = tuple(lidar_values)
        rospy.loginfo(f"Return ... lidar val : {lidar_values}")
        return lidar_values


if __name__ == "__main__":
    rospy.init_node("test recognizer")
    recognizer = Recognizer()

    while not rospy.is_shutdown():
        recognizer.get_lidar_value([22, 202])