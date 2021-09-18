#!/usr/bin/env python3

def cbf(msg):
    rospy.loginfo(f"ranges : {msg.ranges}")
    rospy.loginfo(f"angle_min : {msg.angle_min}")
    rospy.loginfo(f"angle_max : {msg.angle_max}")
    rospy.loginfo(f"range len : {len(msg.ranges)}")

if __name__ == "__main__":
    import rospy
    from sensor_msgs.msg import LaserScan
    rospy.init_node("test_scan")

    scan_sub = rospy.Subscriber("scan", LaserScan, callback=cbf)

    rospy.spin()