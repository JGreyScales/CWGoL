from tkinter import EventType
import Utils, curses
class drawState:
    def __init__(self) -> None:
        pass

    def draw(std, menu):

        # get user input
        event = std.getch() 
        std.addstr(5,5,str(event))
        if event == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
        elif event == 10:
            pass
        elif event == 27:
            std.clear()
            return 0

        # check and update states




        #cycle
        std.refresh()



        return 1