#!/usr/bin/env python3

from lotti_nav.srv import WhereIgo
import rospy

def request_destination(request):
    rospy.wait_for_service("Where_I_go")
    des_requester = rospy.ServiceProxy("Where_I_go", WhereIgo)
    rospy.loginfo(f"Request destination")
    destination = des_requester(1)
    rospy.loginfo(f"Recevied destination {destination}")

    return destination

if __name__ == "__main__":
    import sys
    rospy.init_node("test_service_client")
    req = int(sys.argv[1])
    response = request_destination(req)

    rospy.loginfo(f"end")