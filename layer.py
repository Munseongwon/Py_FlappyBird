from enum import IntEnum, auto
class Layer(IntEnum):
    BACKGROUND = auto()  # BACKGROUND = 1
    OBSTACLE = auto()    # OBSTACLE =2
    FLOOR = auto()       # FLOOR = 3
    PLAYER = auto()      # PLAYER = 4
    UI = auto()          # UI = 5