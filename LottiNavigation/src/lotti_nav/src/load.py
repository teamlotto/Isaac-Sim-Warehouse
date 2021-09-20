#!/usr/bin/env python3

from ast import literal_eval
from logging import RootLogger, error
from numpy.core.numeric import roll
from yaml import load
from rospy.core import loginfo, rospyinfo
from sensor_msgs.msg import JointState, LaserScan, Image
from way_points_manager import WayPointsManager
from move_control import MoveController
from geometry_msgs.msg import Twist
import rospy
import numpy as np


class Loader:
    def __init__(self, joint_name: str = "lift_joint"):
        self.joint_name = joint_name
        self.joint_command = JointState()
        self.joint_command.name = [self.joint_name]
        self.roll, self.pitch, self.yaw = 0., 0., 0.

    def lift_up_down(self, target_pos: float = 0.0, timeout: float = 3.) -> bool:
        """
        Lift 장치를 올리고 내리는 기능
        param: target_pos : float, lifting target position value
        """
        def get_lift_pos():
            joint_state_msg = rospy.wait_for_message("/joint_states", JointState, timeout=10)
            joint_idx = joint_state_msg.name.index(self.joint_name)
            joint_pos = joint_state_msg.position[joint_idx]

            return round(joint_pos * 100, 2)
        
        
        rospy.loginfo(f"target position : {target_pos}")
        pub = rospy.Publisher("/joint_command", JointState, queue_size=1)
        joint_pos = get_lift_pos()
        
        start = rospy.Time.now().to_sec()
        while target_pos != joint_pos:
            joint_pos = get_lift_pos()
            rospy.loginfo(f"Received Current position: {joint_pos}")
            self.joint_command.position = np.array([target_pos])
            pub.publish(self.joint_command)
            rospy.loginfo(f"time :{rospy.Time.now().to_sec() - start}")
            if (rospy.Time.now().to_sec() - start) > timeout:
                return False 
        
        return True

    def rotate(self, angluar_speed, target_angle, extra_val = 56, clock_wise=True, degree=False):
        import math
        PI = math.pi
        pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        vel_msg = Twist()
        try:
            rad_speed = angluar_speed * PI / 180 if degree else angluar_speed
            rad_angle = target_angle * PI / 180 if degree else target_angle
            rad_angle += extra_val * PI / 180
            rospy.loginfo(f"Plus extra_val : {extra_val} rad/s")

            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0

            if clock_wise :
                vel_msg.angular.z = -abs(rad_speed)
            else:
                vel_msg.angular.z = abs(rad_speed)

            import time
            current_angle = 0
            prev_time = time.time()
            rate = rospy.Rate(10)
            while(current_angle < rad_angle):
                rospy.loginfo(f"Rotating ... current_angle {current_angle} -> target_angle {rad_angle}")
                pub.publish(vel_msg)
                current_angle = rad_speed * (time.time() - prev_time)
                rate.sleep()
            
            vel_msg.angular.z = 0
            pub.publish(vel_msg)
            rospy.loginfo(f"Rotating Success")
        except Exception as e:
            rospy.loginfo(f"Error : {e}")
            return False

        return True

    def go_with_vel(self, angular_vel=[0., 0., 0.], linear_vel=[0., 0., 0.]):
        rospy.loginfo(f"Go with angular_vel :{angular_vel}")
        rospy.loginfo(f"Go with linear_vel :{linear_vel}")
        pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        vel_msg = Twist()
        vel_msg.angular.x = angular_vel[0]
        vel_msg.angular.y = angular_vel[1]
        vel_msg.angular.z = angular_vel[2]
        vel_msg.linear.x = linear_vel[0]
        vel_msg.linear.y = linear_vel[1]
        vel_msg.linear.z = linear_vel[2]
        rospy.loginfo(f"vel_msg : \n{vel_msg}")

        import time
        start = time.time()
        while (time.time() - start) < 0.45:
            pub.publish(vel_msg)

        rospy.loginfo(f"Sucess vel msg pub")

    def get_bbox_info(self) -> dict:
        from darknet_ros_msgs.msg import BoundingBoxes
        from collections import defaultdict
        
        msg = rospy.wait_for_message("/darknet_ros/bounding_boxes", BoundingBoxes, timeout=2)
        bbox_dict = defaultdict(list)
        [ bbox_dict[info.Class].append((round(info.probability, 3), info.xmin, info.ymin, info.xmax, info.ymax)) for info in msg.bounding_boxes ]
        
        return bbox_dict

    def get_bbox_center(self, class_name: str) -> dict:
        bbox_dict = self.get_bbox_info()
        center_dict = {}
        for idx, infos in enumerate(bbox_dict[class_name]):
            _, xmin, ymin, xmax, ymax = infos
            center_dict[idx] = (xmin + (xmax - xmin) // 2, ymin + (ymax - ymin) // 2)
        
        return center_dict

    def get_matched_rolltianer_center(self, product_name: str) -> tuple:
        """
        해당 제품의 롤테이너 입구의 센터를 알려주는 함수
        왼쪽 순서대로 rolltainer의 bbox 중앙좌표와 제품의 bbox 중앙좌표의 차이가 가장 작은 것과 매칭 시켜준다.
        매칭의 결과는 중앙 좌표의 매칭이다.
        """
        rolltainer_center_dict = self.get_bbox_center("rolltainer")
        product_center_dict = self.get_bbox_center(product_name)
        rospy.loginfo(f"product {product_name} , {product_center_dict}")
        prd_x_center, _ = product_center_dict[0]
        diff_list = list(map(lambda x: (abs(prd_x_center - x[0]), x[1]), rolltainer_center_dict.values()))
        matched_rolltainer_center = rolltainer_center_dict[diff_list.index(min(diff_list))]

        return matched_rolltainer_center
        
    def match_image_center(self, center, img_hw: tuple = (1280, 750), error_bound = 3):
        w, _ = img_hw
        rospy.loginfo(f"Matching center ... {w // 2 - error_bound} {center[0]} {w // 2 + error_bound}")
        if w // 2 - error_bound < center[0] < w // 2 + error_bound:
            return True
        else:
            return False

    def get_lidar_value(self, idxes:list = [], left_thr=0.3, right_thr=0.6) -> tuple:
        msg = rospy.wait_for_message("/scan", LaserScan, timeout=2)
        rospy.loginfo(f"Got ... range length : {len(msg.ranges)}")
        lidar_values = [ msg.ranges[idx] for idx in idxes ] if idxes else msg.ranges
        lidar_values = tuple(lidar_values)
        rospy.loginfo(f"Return ... lidar val : {lidar_values}")
        return lidar_values

    def enter_with_lidar(self, criteria_vales: list = (22, 202), range_degree: int = 12, left_thr= 1., right_thr = 1.):
        left_criteria, right_criteria = criteria_vales
        # left_lidar_criterias = [left_criteria + i for i in range(range_degree // 2 * -1, range_degree // 2 + 1)]
        # right_lidar_criterais = [right_criteria + i for i in range(range_degree // 2 * -1, range_degree // 2 + 1)]
        # lidar_values = self.get_lidar_value(left_lidar_criterias.extend(right_lidar_criterais))

        # left, right = min(lidar_values[:len(lidar_values) // 2]), min(lidar_values[len(lidar_values) // 2:])
        # rospy.loginfo(f"Got ... Left lidar get : {left} at {list(lidar_values[:len(lidar_values) // 2]).index(left)}")
        # rospy.loginfo(f"Got ... Right lidar get : {right} at {list(lidar_values[len(lidar_values) // 2:]).index(right)}")
        left, right = 777, 777
        while left > left_thr or right > right_thr:
            left, right = self.get_lidar_value((left_criteria, right_criteria))

            if left < left_thr:
                if right > right_thr:
                    self.go_with_vel(angular_vel=[0., 0., -0.07])
                else:
                    self.go_with_vel(linear_vel=[0.07, 0., 0.])
                    
            elif right < right_thr:
                if left > left_thr:
                    self.go_with_vel(angular_vel=[0., 0., 0.07])
                else:
                    self.go_with_vel(linear_vel=[0.07, 0., 0.])

            else:
                self.go_with_vel(linear_vel=[0.07, 0., 0.])
            
        rospy.sleep(3)

        left, right = 777, 777
        while left > left_thr or right > right_thr:
            left, right = self.get_lidar_value((left_criteria, right_criteria))

            if left < left_thr:
                if right > right_thr:
                    self.go_with_vel(angular_vel=[0., 0., -0.07])
                else:
                    self.go_with_vel(linear_vel=[0.07, 0., 0.])
                    
            elif right < right_thr:
                if left > left_thr:
                    self.go_with_vel(angular_vel=[0., 0., 0.07])
                else:
                    self.go_with_vel(linear_vel=[0.07, 0., 0.])

            else:
                self.go_with_vel(linear_vel=[0.07, 0., 0.])
        
        rospy.sleep(7)

        self.go_with_vel()

    def enter_rolltainer(self):
        import math
        # target_product_name = "blue"
        target_product_name = "red"
        # direction = "right"
        direction = "left"
        center = (-1, -1)
        clock_dir = True if direction == "right" else False
        target_radian = 90 * 2 * math.pi / 360
        # rotate_ret = self.rotate(0.2, target_radian, degree=False, clock_wise=clock_dir)
        rotate_ret = True
        self.go_with_vel(linear_vel=[0.5, 0., 0.]) if rotate_ret else self.go_with_vel(linear_vel=[0., 0., 0.])

        while not self.match_image_center(center):
            center = self.get_matched_rolltianer_center(target_product_name)
        
        self.go_with_vel(linear_vel=[0., 0., 0.])
        clock_dir ^= True
        self.rotate(0.2, target_radian, degree=False, clock_wise=clock_dir)
        self.go_with_vel(linear_vel=[0.7, 0., 0.])
        
        rospy.sleep(7)

    def escape_rolltainer(self):
        pass

if __name__ == "__main__":
    import rospy
    rospy.init_node("Loader_test")

    loader = Loader("lift_joint")

    # loader lift_up test
    ## Success
    # ret = loader.lift_up_down(target_pos=4.0, timeout=10.)
    # rospy.loginfo("Lift up Test Success") if ret else rospy.loginfo("Lift up Test Fail")

    # rospy.sleep(2)

    # loader lift_up test
    ## Success
    # ret = loader.lift_up_down(target_pos=0.0, timeout=10.)
    # rospy.loginfo("Lift down Test Success") if ret else rospy.loginfo("Lift down Test Fail")
    
    # rospy.sleep(2)

    # loader lift_up test
    ## Fail
    # ret = loader.lift_up_down(target_pos=4.0, timeout=1.)
    # rospy.loginfo("Lift up Test Success") if ret else rospy.loginfo("Lift up Test Fail")

    # rospy.sleep(2)

    # # loader lift_up test
    ## Fail
    #ret = loader.lift_up_down(target_pos=0.0, timeout=1.)
    #rospy.loginfo("Lift down Test Success") if ret else rospy.loginfo("Lift down Test Fail")

    # zone_manager = WayPointsManager()
    # move_controller = MoveController()

    # pose = zone_manager.get_goods_pose("goods_zone3")
    # ret = move_controller.move_goods_zone(pose)
    import math
    # target = 90 * 2 * math.pi / 360
    # loader.rotate(angluar_speed=0.2, target_angle=target, clock_wise=True, degree=False)
    # loader.go_with_vel(linear_vel=[1., 0., 0.])
    
    # bbox info test
    # result = loader.get_bbox_info()
    # rospy.loginfo(result["red"])

    # center getting test
    # result = loader.get_bbox_center("red")
    # rospy.loginfo(result)

    # matched rolltainer center test
    # result = loader.get_matched_rolltianer_center("red")
    # rospy.loginfo(f"Get matched rolltainer center : {result}") 
    # result = loader.get_matched_rolltianer_center("green")
    # rospy.loginfo(f"Get matched rolltainer center : {result}") 
    # result = loader.get_matched_rolltianer_center("blue")
    # rospy.loginfo(f"Get matched rolltainer center : {result}") 

    # match from center to image center
    # while True:
    #     blue_center = loader.get_matched_rolltianer_center("blue")
    #     rospy.loginfo(blue_center)
    #     if loader.match_image_center(blue_center):
    #         rospy.loginfo("matched")
    #     else:
    #         rospy.loginfo("not matched")
    
    # entering test
    loader.enter_rolltainer()
    # while True:
    #     loader.get_lidar_value(idxes=(22, 201, 202,203,204))

    # entering with lidar test
    loader.enter_with_lidar()

    ret = loader.lift_up_down(target_pos=10.0, timeout=10.)
    # rospy.loginfo("Lift down Test Success") if ret else rospy.loginfo("Lift down Test Fail")

    rospy.spin()
