#!/usr/bin/env python3

from lotti_nav.srv import *
import rospy
from collections import deque

def callback(req):
    rospy.loginfo(f"Server was Recieved Request from LOTTI : {req.request}")
    response = None
    zone_goods = [9, 6]
    zone_def = ['goods_zone2', 'goods_zone3']
    if req.request == 'ready':
        response = zone_def[zone_goods.index(min(zone_goods))]
        rospy.loginfo(f"Server will sending Response to LOTTI : {response}")
    elif req.request != 'ready' and req.request != None:
        queue_state = eval(f'q_{req.request}')
        if len(queue_state) > 0:
            response = queue_state.popleft()
        else:
            rospy.loginfo(f"load zone {req.request} are fully occupied")
    else:
        return None
    return WhereIgoResponse(response)

def main():
    s = rospy.Service("Where_I_go", WhereIgo, callback)
    rospy.loginfo("Server response")

if __name__ == "__main__":
    q_red = deque(['load_red_1', 'load_red_2', 'load_red_3', 'load_red_4'])
    q_green = deque(['load_green_1', 'load_green_2', 'load_green_3', 'load_green_4'])
    q_blue = deque(['load_blue_1', 'load_blue_2', 'load_blue_3', 'load_blue_4', ])

    rospy.init_node("LottoWorld_server")

    main()

    rospy.spin()    
