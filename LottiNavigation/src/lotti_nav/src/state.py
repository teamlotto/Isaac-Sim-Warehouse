from enum import IntEnum

class StateManager(IntEnum):
    Drive: int = 0
    Wait: int = 1
    Recognition: int = 2
    Load: int = 3

if __name__ == "__main__":
    manager = StateManager
    print(manager.Drive == 0)
    print(manager.Wait == 1)
    print(manager.Recognition == 2)
    print(manager.Load == 3)