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
        except UnboundLocalError as e:
            return -1
        return position

    def get_wait_pos(self, name: str) -> tuple:
        try:
            position = self.wait_zone_position[name]
        except UnboundLocalError as e:
            return -1
        return position

    def get_load_pos(self, name: str) -> tuple:
        pass

if __name__ == "__main__":
    zone_manage = WayPointsManager()
    
    # get_goods_pos test area
    if zone_manage.get_goods_pos("goods_zone2") != -1:
        print(True)
    if zone_manage.get_goods_pos("goods_zone3") != -1:
        print(True)
    print(zone_manage.get_wait_pos("wait_zone1"))
    print(zone_manage.get_goods_pos("goods_zone5"))
