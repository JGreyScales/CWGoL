import curses
from Utils import functions
class cycleState:
    def __init__(self) -> None:
        pass

    def sceneCycle(std):
        std.timeout(1000)
        std.getch()

        functions.getNearby(std)