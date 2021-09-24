#!/usr/bin/env python3

from rospy.topics import Publisher
from sensor_msgs.msg import JointState
from move_control import MoveController
from recognize import Recognizer
import rospy
import numpy as np


class Loader:
    def __init__(self, recognizer, move_controller, joint_name: str = "lift_joint"):
        self.joint_name = joint_name
        self.joint_command = JointState()
        self.joint_command.name = [self.joint_name]
        self.roll, self.pitch, self.yaw = 0., 0., 0.
        self.recognizer = recognizer
        self.move_controller = move_controller

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

    def get_matched_rolltianer_center(self, product_name: str, width_thr: int=175):
        """
        해당 제품의 롤테이너 입구의 센터를 알려주는 함수
        왼쪽 순서대로 rolltainer의 bbox 중앙좌표와 제품의 bbox 중앙좌표의 차이가 가장 작은 것과 매칭 시켜준다.
        매칭의 결과는 중앙 좌표의 매칭이다.
        """
        rolltainer_center_dict = self.recognizer.get_bbox_center("rolltainer", width_thr=width_thr)
        product_center_dict = self.recognizer.get_bbox_center(product_name)
        rospy.loginfo(f"product {product_name} , {product_center_dict}")
        if product_center_dict != {} and rolltainer_center_dict != {}:
            idx_key = min(product_center_dict.keys())
            prd_x_center, _ = product_center_dict[idx_key]
            diff_list = list(map(lambda x: (abs(prd_x_center - x[0])), rolltainer_center_dict.values()))
            rospy.loginfo(f"Test diff list : {diff_list}")
            target_idx = diff_list.index(min(diff_list))
            matched_rolltainer_center = rolltainer_center_dict[target_idx]

            return target_idx, matched_rolltainer_center
        return None, None

    def get_matched_rolltainer_width(self, cls_name: str, target_idx:int, width_thr:int=175):
        bbox_width_dict = self.recognizer.get_bbox_width(cls_name, width_thr=width_thr)
        if bbox_width_dict != {} and target_idx in bbox_width_dict.keys():
            return bbox_width_dict[target_idx]
        return None

    def enter_with_lidar(self, criteria_vales: list = (22, 202), range_degree: int = 12, left_thr= 1.2, right_thr = 1.2, timeout:int =30):
        left_criteria, right_criteria = criteria_vales
        def control_with_lidar(left_angular_vel:list, left_linear_vel:list, right_angular_vel:list, right_linear_vel:list, center_linear_vel:list =[0.07, 0., 0.], timeout:int = 30):
            import time
            left, right = 777, 777
            start = time.time()
            is_timeout = False
            while left > left_thr or right > right_thr:
                left, right = self.recognizer.get_lidar_value((left_criteria, right_criteria))
                
                if left < left_thr:
                    if right > right_thr:
                        if left < 0.14:
                            rospy.loginfo("So Close, Took care of it -> time out ")
                            is_timeout = True
                            break
                        else:
                            self.move_controller.go_with_vel(angular_vel=left_angular_vel)
                    else:
                        self.move_controller.go_with_vel(linear_vel=left_linear_vel)
                        
                elif right < right_thr:
                    if left > left_thr:
                        if right < 0.14:
                            rospy.loginfo("So Close, Took care of it -> time out ")
                            is_timeout = True
                            break
                        else:
                            self.move_controller.go_with_vel(angular_vel=right_angular_vel)
                    else:
                        self.move_controller.go_with_vel(linear_vel=right_linear_vel)
                else:
                    self.move_controller.go_with_vel(linear_vel=center_linear_vel)

                rospy.loginfo(f"Time ... {time.time() - start}")
                if time.time() - start > timeout:
                    rospy.loginfo("TIme out")
                    is_timeout = True
                    break
            return is_timeout

        self.move_controller.go_with_vel(linear_vel=[0.4, 0., 0.])
        rospy.sleep(2)
        ret = control_with_lidar(left_angular_vel=[0., 0., -0.07], left_linear_vel=[0.07, 0., 0.], right_angular_vel=[0., 0., 0.07], right_linear_vel=[0.07, 0., 0.], timeout=timeout)
        if ret:
            return False
        rospy.sleep(3)
        ret = control_with_lidar(left_angular_vel=[0., 0., -0.07], left_linear_vel=[0.07, 0., 0.], right_angular_vel=[0., 0., 0.07], right_linear_vel=[0.07, 0., 0.], timeout=timeout)
        if ret:
            return False
        rospy.sleep(7)
        self.move_controller.go_with_vel()

        return True
        
    def enter_with_cam(self, target_product_name:str = "green", function_timeout: float = 28., left_case_timeout: float= 2., right_case_timeout: float = 2., bbox_width_thr: int = 670):
        def go_to_center_with_cam(cur_center, angular_vel: list, linear_vel: list):
            self.move_controller.go_with_vel(angular_vel=angular_vel, linear_vel=linear_vel)
            _, tmp = self.get_matched_rolltianer_center(target_product_name, width_thr=280)
            matched_center = tmp if tmp is not None else cur_center
            return matched_center

        import time
        self.move_controller.go_with_vel(linear_vel=[0.5, 0., 0.])
        rospy.sleep(4)
        img_center = self.recognizer.img_w_h[0] // 2, self.recognizer.img_w_h[1] // 2
        center = (0, 0)
        rolltainer_bbox_width = 0
        prg_start = time.time()
        while center is not None and time.time() - prg_start < function_timeout and rolltainer_bbox_width < bbox_width_thr:
            start = time.time()
            idx, tmp = self.get_matched_rolltianer_center(target_product_name, width_thr=280)
            center = tmp if tmp is not None else center
            rospy.loginfo(f"mtached center : {center}")
            if idx is not None:
                tmp = self.get_matched_rolltainer_width("rolltainer", idx, width_thr=280)
                rolltainer_bbox_width = tmp if tmp is not None else rolltainer_bbox_width
            else:
                pass
            rospy.loginfo(f"bbox width : {rolltainer_bbox_width}")
            
            left_right = self.recognizer.is_left_right(img_center, center, error_bound=16)
            if left_right:
                rospy.loginfo("Left")
                while not self.recognizer.match_image_center(center, error_bound=10) and time.time() - start < left_case_timeout:
                    center = go_to_center_with_cam(cur_center=center, angular_vel=[0., 0., 0.1], linear_vel=[0.2, 0., 0.])
            elif left_right is None:
                rospy.loginfo("Good Pose")
                center = go_to_center_with_cam(cur_center=center, angular_vel=[0., 0., 0.], linear_vel=[0.3, 0., 0.])

            else:
                rospy.loginfo("Right")
                while not self.recognizer.match_image_center(center, error_bound=10) and time.time() - start < right_case_timeout:
                    center = go_to_center_with_cam(cur_center=center, angular_vel=[0., 0., -0.1], linear_vel=[0.2, 0., 0.])

        rospy.loginfo("enter with cam End...")
        self.move_controller.go_with_vel()
                
    def enter_rolltainer(self, target_product_name:str = "blue", direction: str = "right"):
        rospy.sleep(2)
        import math
        import time
        import os
        from std_msgs.msg import Int32

        if direction == "right":
            clock_dir = True
        elif direction == "left":
            clock_dir = False
        else:
            clock_dir = None
        rospy.loginfo(f"target_product_name : {target_product_name}")
        rospy.loginfo(f"direction : {direction}")
        pub_dict = {"middle": 0, "right": 2, "left": 1}
        topic_name = "which_launch"
        if clock_dir is not None:
            target_radian = 90 * math.pi / 180

            os.system(f"rostopic pub -1 {topic_name} std_msgs/Int32 {pub_dict[direction]}")
            rospy.sleep(5)
            rospy.loginfo(f"Send darknet_ros mode : {pub_dict[direction]}")
            _ = self.move_controller.rotate(0.2, target_radian, degree=False, clock_wise=clock_dir)

            self.move_controller.go_with_vel(linear_vel=[0.5, 0., 0.])
            center = (-1, -1)
            while not self.recognizer.match_image_center(center, error_bound=10):
                _, tmp = self.get_matched_rolltianer_center(target_product_name)
                center = tmp if tmp is not None else center

            self.move_controller.go_with_vel()
            clock_dir ^= True
            _ = self.move_controller.rotate(0.2, target_radian, degree=False, clock_wise=clock_dir)

        os.system(f"rostopic pub -1 {topic_name} std_msgs/Int32 {pub_dict['middle']}")
        rospy.sleep(5)
        
        while True:
            self.enter_with_cam(target_product_name=target_product_name, function_timeout=12., left_case_timeout=2., right_case_timeout=2.)
            result = self.enter_with_lidar(criteria_vales=[22, 202], left_thr=1., right_thr=1., timeout=90.)
            if result:
                break
            else:
                self.move_controller.go_with_vel(linear_vel=[-0.7, 0. ,0.])
                rospy.sleep(11)
        
        rospy.sleep(7)
        rospy.loginfo("Entering Container Sucess !")

    def escape_rolltainer(self):
        self.move_controller.go_with_vel(linear_vel=[-0.5, 0., 0.])
        rospy.sleep(15)
        self.move_controller.go_with_vel()

if __name__ == "__main__":
    import rospy
    rospy.init_node("Loader_test")
    from move_control import MoveController
    from recognize import Recognizer

    loader = Loader(move_controller=MoveController(), recognizer=Recognizer(), joint_name="lift_joint")

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
    # loader.enter_with_cam()
    # while True:
    #     loader.get_lidar_value(idxes=(22, 201, 202,203,204))

    # entering with lidar test
    # loader.enter_with_lidar()

    # ret = loader.lift_up_down(target_pos=10.0, timeout=10.)
    # rospy.loginfo("Lift down Test Success") if ret else rospy.loginfo("Lift down Test Fail")
    # rospy.sleep(5)
    # ret = loader.lift_up_down(target_pos=0., timeout=10.)

    loader.enter_rolltainer(target_product_name="blue", direction="right")
    # loader.enter_with_lidar()
    rospy.spin()
