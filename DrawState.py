import curses
class drawState:
    def draw(std):
        # get user input

        event = std.getch() 
        if event == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
            # create banner to allow for info text
            if my > 0:
                x = std.inch(my, mx)
                std.addstr(0,0, f"char:{x} Pos:{my},{mx}")

                if x == 9608:
                    std.addch(my, mx, ' ')
                    std.refresh()
                else:
                    std.addstr(my, mx, "█")

        elif event == 10:
            _, xMax = std.getmaxyx()
            for i in range(0, xMax):
                std.addch(0, i, ' ')
            return 2
        elif event == 27:
            std.clear()
            return 0
            
        #cycle
        std.refresh()
        return 1