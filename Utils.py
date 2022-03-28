import curses

class functions:
    def __init__(self) -> None:
        pass

    def rectangle(std, uly, ulx, lry, lrx):
#       taken from:
#       https://www.programcreek.com/python/?project_name=ShikyoKira%2FProject-New-Reign---Nemesis-Main
        std.vline(uly+1, ulx, curses.ACS_VLINE, lry - uly - 1)
        std.hline(uly, ulx+1, curses.ACS_HLINE, lrx - ulx - 1)
        std.hline(lry, ulx+1, curses.ACS_HLINE, lrx - ulx - 1)
        std.vline(uly+1, lrx, curses.ACS_VLINE, lry - uly - 1)

        std.addch(uly, ulx, curses.ACS_ULCORNER)
        std.addch(uly, lrx, curses.ACS_URCORNER)
        std.addch(lry, lrx, curses.ACS_LRCORNER)
        std.addch(lry, ulx, curses.ACS_LLCORNER) 


    def refresh(loadState, std):
            if loadState == 0:
                std.refresh()
                return None
            else:
                return std.getch()

    def select(buttons):
        for i in buttons:
            if buttons[i]:
                count = 1
                for j in buttons:
                    if i == j: return count
                    count += 1

    def getNearby(std):
        pass