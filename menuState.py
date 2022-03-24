import curses
from Utils import functions
class menuState:
    def __init__(self):
        pass


    def menu(std, bitch, substate, loadState = bool):

        # UI effects
        functions.rectangle(std, 3, 109, 18, 129)
        std.border()

        # creates text onto the std
        count = 1
        for fuck in list(bitch):
            std.addstr(5 * (list(bitch).index(fuck) + 1), 119 - round(len(fuck)/2) - 2, str(count) + '. ' + str(fuck), curses.color_pair(int(bitch[fuck])))
            count += 1

        keyPress = functions.refresh(loadState, std)

        # cycle to selected key
        if keyPress == 49:
            bitch |= {"Start":True, "Rules":False, "Exit":False}
        elif keyPress == 50:
            bitch |= {"Start":False, "Rules":True, "Exit":False}
        elif keyPress == 51:
            bitch |= {"Start":False, "Rules":False, "Exit":True}



        # if player selects
        elif keyPress == 10:

            x = functions.select(bitch)


            # apply the different assigned functions
            if x == 1:
                std.clear()
                return [bitch, loadState, 1]

            elif x == 2:
                
                rules = ["1. Any live cell with two or three live neighbours survives.",
                        "2. Any dead cell with three live neighbours becomes a live cell.",
                        "3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.",
                        "Once the game is started, press ENTER to begin the sim; press ESC to pause or return to drawstate"]

                for i in range(len(rules)):
                    std.addstr((5 * i) + 30,  119 - round(len(rules[i]) / 2 ), rules[i])
                    std.timeout(25)
                    std.getch()

            elif x == 3:
                curses.endwind()

        return [bitch, loadState, 0]
