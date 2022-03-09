#external imports
from curses import wrapper
import curses, ctypes
from turtle import st

#Internal Imports
from menuState import menuState
from DrawState import drawState
from CycleState import cycleState

ctypes.WinDLL('user32').ShowWindow(ctypes.WinDLL('kernel32').GetConsoleWindow(), 3)


def main(std, board=[["", 0]* 253] * 66):
    # curse init
    curses.LINES = 66

    # pair inits
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # var inits
    state, oldState = 0, 0 
    text = {
            "Start": [1, True],
            "Rules": [2, False],
            "Exit": [2, False]
            }

    # game loops
    while True:
        std.clear()
        if oldState != state:
            loadState = 0

        # if paused
        if state == 0:
                text, loadState = menuState.menu(std, text)
                std.refresh()

        elif state == 1:
            drawState.draw()

        elif state == 2:
            cycleState.sceneCycle()

        oldState = state

wrapper(main)