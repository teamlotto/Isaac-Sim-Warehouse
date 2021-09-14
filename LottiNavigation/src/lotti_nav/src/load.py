#!/usr/bin/env python3

from rospy.core import loginfo
from sensor_msgs.msg import JointState
from pid import PID
import rospy
import numpy as np


class Loader:
    def __init__(self, joint_name: str = "lift_joint"):
        self.joint_name = joint_name
        self.joint_command = JointState()
        self.joint_command.name = [self.joint_name]
        rospy.loginfo(f"Loader was Received joint name : {self.joint_command.name}")
        self.lift_success, self.first = False, True

    def lift_up_down(self, target_pos: float = 0.0, timeout: float = 3.) -> bool:
        """
        Lift 장치를 올리고 내리는 기능
        param: target_pos : float, lifting target position value
        """
        def get_lift_pos():
            joint_state_msg = rospy.wait_for_message("/joint_states", JointState, timeout=1)
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

    def enter_rolltainer(self):
        pass

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
