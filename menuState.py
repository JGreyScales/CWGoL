import curses
from Utils import functions
class menuState:
    def __init__(self):
        pass

    def menu(std, bitch = dict, loadState = bool):



        
        functions.rectangle(std, 3, 109, 18, 129)
        std.border()

        # creates text onto the std
        for fuck in list(bitch.keys()):
            std.addstr(5 * (list(bitch.keys()).index(fuck) + 1), 119 - round(len(fuck)/2), fuck, curses.color_pair(bitch[fuck][0]))

        # returns keyboard '8-bit' representation???? i think?
        # Returns none for loadstate
        x = functions.refresh(loadState, std)

        return [bitch, loadState]
