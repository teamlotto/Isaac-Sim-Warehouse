class WayPointsManager:
    def __init__(self) -> None:
        self.goods_zone_position = {
            "goods_zone2" : (1,1),
            "goods_zone3" : (2,2),
        }

        self.wait_zone_position = {
            "wait_zone1" : (0,0),
        }

        self.load_zone_position = {
            "load_zone1" : (3.5,3.5),
            "load_zone2" : (4.5,4.5),
            "load_zone3" : (5.5,5.5),
        }

    def get_goods_pos(self, name: str) -> tuple:
        try:
            position = self.goods_zone_position[name]
        except UnboundLocalError:
            return -1
        except KeyError:
            return -1
        return position

    def get_wait_pos(self, name: str) -> tuple:
        try:
            position = self.wait_zone_position[name]
        except UnboundLocalError:
            return -1
        except KeyError:
            return -1
        return position

    def get_load_pos(self, name: str) -> tuple:
        pass

if __name__ == "__main__":
    zone_manage = WayPointsManager()
    
    # get_goods_pos test area
    result = zone_manage.get_goods_pos("goods_zone2")
    if result == (1,1):
        print("test in success")
    elif result == -1:
        print("exceptional in success")
    else:
        print("test failed") 

    result = zone_manage.get_goods_pos("goods_zone3")
    if result == (2,2):
        print("test in success")
    elif result == -1:
        print("exceptional in success")
    else:
        print("test failed") 
    
    result = zone_manage.get_goods_pos("goods_zone5")
    if result == (1,1):
        print("test in success")
    elif result == -1:
        print("exceptional in success")
    else:
        print("test failed") 

    result = zone_manage.get_goods_pos(1)
    if result == (1,1):
        print("test in success")
    elif result == -1:
        print("exceptional in success")
    else:
        print("test failed") 

    #get_wait_pos test area
    result = zone_manage.get_wait_pos("wait_zone1")
    if result == (0,0):
        print("test in success")
    elif result == -1:
        print("exceptional in success")
    else:
        print("test failed")

    result = zone_manage.get_wait_pos("zone1")
    if result == (0,0):
        print("test in success")
    elif result == -1:
        print("exceptional in success")
    else:
        print("test failed")

    result = zone_manage.get_wait_pos(1)
    if result == (0,0):
        print("test in success")
    elif result == -1:
        print("exceptional in success")
    else:
        print("test failed")
