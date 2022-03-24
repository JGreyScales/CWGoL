#external imports
from curses import wrapper
import curses, ctypes
from os import stat
from sre_parse import State


#Internal Imports
from menuState import menuState
from DrawState import drawState
from CycleState import cycleState

ctypes.WinDLL('user32').ShowWindow(ctypes.WinDLL('kernel32').GetConsoleWindow(), 3)


def main(std, board=[["", 0]* 253] * 66):
    # curse init
    curses.LINES = 66
    curses.curs_set(0)
    

    # pair inits
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # var inits
    state, oldState, keyPress, substate = 0, 0, 0, 0
    menu = [['o'] * 228] * 66
    text = {
            "Start": True,
            "Rules": False,
            "Exit": False
            }

    # game loops
    while True:
        #std.clear()

        if oldState != state:
            loadState = 0

        # if paused
        if state == 0:
            curses.mousemask(0)
            text, loadState, state = menuState.menu(std, text, substate)
            std.refresh()

        # if drawing
        elif state == 1:
            curses.mousemask(1)
            state = drawState.draw(std, menu)

        # if running
        elif state == 2:
            curses.mousemask(0)
            cycleState.sceneCycle()

        oldState = state


wrapper(main)