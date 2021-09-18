#!/usr/bin/env python3

from lotti_nav.srv import *
import rospy

def callback(req):
    rospy.loginfo(f"Server was Recieved Request from LOTTI : {req.request}")
    response = None
    if req.request == 1:
        response = "goods_zone3"
        rospy.loginfo(f"Server will sending Response to LOTTI : {response}")
    else:
        return None
    return WhereIgoResponse(response)

def main():
    s = rospy.Service("Where_I_go", WhereIgo, callback)
    rospy.loginfo("Server respose")

if __name__ == "__main__":
    rospy.init_node("LottoWorld_server")
    main()
    rospy.spin()
    