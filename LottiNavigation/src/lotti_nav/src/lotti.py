from state import StateManager
from move_control import MoveController
from way_points_manager import WayPointsManager
import rospy

class Lotti:
    def __init__(self):
        self.zone_manager = WayPointsManager()
        self.move_controller = MoveController()
        self.state = StateManager.Wait

    def operate(self):
        while True:
            # Wait State
            if self.state == StateManager.Wait:
                pose = self.zone_manager.get_wait_pose('wait_zone1')
                ret = self.move_controller.move_wait_zone(pose)
                if ret:
                    self.state = StateManager.Drive
            
            # Drive State
            elif self.state == StateManager.Drive:
                pose = self.zone_manager.get_goods_pose('goods_zone2')
                ret = self.move_controller.move_goods_zone(pose)
                if ret:
                    self.state = StateManager.Recognition

            # Recognition State
            elif self.state == StateManager.Recognition:
                rospy.info("Recognition State")
                self.state = StateManager.Load
            
            # Load State
            elif self.state == StateManager.Load:
                rospy.info("Load State")
                pose = self.zone_manager.get_load_pose(' ')
                ret = self.move_controller.move_load_zone(pose)
                if ret:
                    pose = self.zone_manager.get_wait_pose(' ')
                    ret = self.move_controller.move_wait_zone(pose)
                    if ret:
                        self.state = StateManager.Wait
        

if __name__ == "__main__":
    lotti = Lotti()
    lotti.operate()
                
