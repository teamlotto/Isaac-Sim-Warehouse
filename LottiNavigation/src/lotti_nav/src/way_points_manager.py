class WayPointsManager:
    def __init__(self):
        self.goods_zone_pose = {
            "goods_zone2" : [(0.549774169922, -7.30722618103, 0), (0, 0, -0.707685951917, 0.706527135685)],
            "goods_zone3" : [(1.03079235554, 10.0041303635, 0), (0, 0, 0.706575209569, 0.707637953492)],
        }

        self.wait_zone_pose = {
            "wait_zone1" : [(9.37379264832, 1.04199016094, 0), (0, 0, -0.00170161574453, 0.999998552251)],
        }

        self.load_zone_pose = {
            "load_red" : [(-7.94609212875, -4.41245365143, 0), (0, 0, 0.999999957188, 0.000292615090281)],
            "load_green" : [(-7.88964653015, 1.26279211044, 0), (0, 0, 0.999999984339, 0.000176982082669)],
            "load_blue" : [(-7.97520112991, 7.12481021881, 0), (0, 0, 0.999819333077, -0.0190079248165)],
        }

    def get_goods_pose(self, name: str) -> list:
        try:
            pose = self.goods_zone_pose[name]
        except UnboundLocalError:
            return -1
        except KeyError:
            return -1
        return pose

    def get_wait_pose(self, name: str) -> list:
        try:
            pose = self.wait_zone_pose[name]
        except UnboundLocalError:
            return -1
        except KeyError:
            return -1
        return pose

    def get_load_pose(self, name: str) -> list:
        try:
            pose = self.load_zone_pose[name]
        except UnboundLocalError:
            return -1
        except KeyError:
            return -1
        return pose

if __name__ == "__main__":
    zone_manage = WayPointsManager()
    
    # get_goods_pose test area
    result = zone_manage.get_goods_pose("goods_zone2")
    if result == [(2.38019895554, 0.451567530632, 0), (0, 0, 0.0127541419977, 0.999918662623)]:
        print("test in success")
    elif result == -1:
        print("exceptional in success")
    else:
        print("test failed") 

    result = zone_manage.get_goods_pose("goods_zone3")
    if result == [(-5.19693231583, 0.163684234023, 0), (0, 0, 0.999999851758, -0.000544504296372)]:
        print("test in success")
    elif result == -1:
        print("exceptional in success")
    else:
        print("test failed") 
    
    result = zone_manage.get_goods_pose("goods_zone5")
    if result == -1:
        print("exceptional in success")
    else:
        print("test failed") 

    result = zone_manage.get_goods_pose(1)
    if result == -1:
        print("exceptional in success")
    else:
        print("test failed") 

    #get_wait_pose test area
    result = zone_manage.get_wait_pose("wait_zone1")
    if result == [(-1.07045590878, 6.2899055481, 0), (0, 0, -0.701823194244, 0.712351180262)]:
        print("test in success")
    elif result == -1:
        print("exceptional in success")
    else:
        print("test failed")

    result = zone_manage.get_wait_pose("zone1")
    if result == -1:
        print("exceptional in success")
    else:
        print("test failed")

    result = zone_manage.get_wait_pose(1)
    if result == -1:
        print("exceptional in success")
    else:
        print("test failed")


    #get_load_pose test area
    result = zone_manage.get_load_pose("load_red")
    if result == [(3.0478579998, -4.80341033936, 0), (0, 0, -0.704314478301, 0.709888100798)]:
        print("test in success")
    elif result == -1:
        print("exceptional in success")
    else:
        print("test failed")

    result = zone_manage.get_load_pose("load_green")
    if result == [(-1.04428827763, -4.99190855026, 0), (0, 0, -0.702213206306, 0.711966721757)]:
        print("test in success")
    elif result == -1:
        print("exceptional in success")
    else:
        print("test failed")

    result = zone_manage.get_load_pose("load_blue")
    if result == [(-4.79386806488, -4.82265424728, 0), (0, 0, -0.700243936583, 0.71390365546)]:
        print("test in success")
    elif result == -1:
        print("exceptional in success")
    else:
        print("test failed")

    result = zone_manage.get_load_pose("red")
    if result == -1:
        print("exceptional in success")
    else:
        print("test failed")

    result = zone_manage.get_load_pose(1)
    if result == -1:
        print("exceptional in success")
    else:
        print("test failed")

