#external imports
from curses import wrapper
import curses, ctypes

#Internal Imports
from menuState import menuState
from DrawState import drawState
from CycleState import cycleState

ctypes.WinDLL('user32').ShowWindow(ctypes.WinDLL('kernel32').GetConsoleWindow(), 3)


def cycle(board):
    pass


def main(std, board=[["", 0]* 253] * 66):
    curses.LINES = 66
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)



    std.border()
    state = 0 
    text = {
            "Start": [1, True],
            "Rules": [2, False],
            "Exit": [2, False]
            }


    while True:
        std.clear()

        if state == 0:
                text = menuState.menu(std, text)
                std.refresh()

        elif state == 1:
            drawState.draw()

        elif state == 2:
            cycleState.sceneCycle()

wrapper(main)