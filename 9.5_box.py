class Box:
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

    def __init__(self):
        self.__owner = None
        self.__left_side= False
        self.__right_side = False
        self.__up_side = False
        self.__down_side = False

    def get_owner(self):
        return self.__owner

    def add_owner(self, owner):
        self.__owner = owner

    def has_line_on_side(self, side):
        if side == Box.LEFT:
            return self.__left_side
        elif side == Box.RIGHT:
            return self.__right_side
        elif side == Box.UP:
            return self.__up_side
        else:
            return self.__down_side

    def add_line(self, side):
        if self.has_line_on_side(side) == True:
            return False
        else:
            if side == Box.LEFT:
                self.__left_side = True
            elif side == Box.RIGHT:
                self.__right_side = True
            elif side == Box.UP:
                self.__up_side = True
            else:
                self.__down_side = True
            return True

    def four_lines_placed(self):
        if self.__left_side == True and self.__right_side == True\
                and self.__up_side == True and self.__down_side == True:
            return True
        else:
            return False

