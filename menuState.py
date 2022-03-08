import curses
from re import I

class menuState:
    def __init__(self):
        pass

    def menu(std, bitch = dict):
        for fuck in list(bitch.keys()):
            std.addstr(5 * (list(bitch.keys()).index(fuck) + 1), 119 - round(len(fuck)/2), fuck, curses.color_pair(bitch[fuck][0]))
        std.refresh()
        return bitch
