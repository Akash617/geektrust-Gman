class Gman():
    def __init__(self, x_coordinates, y_coordinates, direction):
        self.__x_coordinates = x_coordinates
        self.__y_coordinates = y_coordinates
        self.__direction = direction
        self.__power = 200
        self.__cost_to_turn = 5
        self.__cost_to_move = 10


    # Check if Gman is on target or not
    def is_on_target(self, x_coordinates, y_coordinates):
        if self.__x_coordinates != x_coordinates or self.__y_coordinates != y_coordinates:
            return False

        return True


    def which_way_to_turn(self, opposite, x_coordinates, y_coordinates):
        if opposite == "EW":
            if (y_coordinates - self.__y_coordinates) < 0:
                return "S"
            else:
                return "N"
        elif opposite == "NS":
            if (x_coordinates - self.__x_coordinates) < 0:
                return "W"
            else:
                return "E"


    # Turn Gman 90 degrees to face a direction he needs to go
    def turn(self, opposite, x_coordinates, y_coordinates):
        self.__direction = self.which_way_to_turn(opposite, x_coordinates, y_coordinates)
        self.__power -= self.__cost_to_turn


    # Move the Gman by 1 step in the direction he's facing
    def move(self, x_coordinates, y_coordinates):
        direction_assocation = {"N": (0,1), "E": (1,0), "S": (0,-1), "W": (-1,0)}

        self.__x_coordinates += direction_assocation[self.__direction][0]
        self.__y_coordinates += direction_assocation[self.__direction][1]

        self.__power -= self.__cost_to_move


    # Decide if the Gman needs to turn or if he can move in the direction he's facing
    def turn_or_move(self, x_coordinates, y_coordinates):
        if self.__direction == "E" and (x_coordinates - self.__x_coordinates) <= 0:
            self.turn("EW", x_coordinates, y_coordinates)
        elif self.__direction == "W" and (x_coordinates - self.__x_coordinates) >= 0:
            self.turn("EW", x_coordinates, y_coordinates)
        elif self.__direction == "N" and (y_coordinates - self.__y_coordinates) <= 0:
            self.turn("NS", x_coordinates, y_coordinates)
        elif self.__direction == "S" and (y_coordinates - self.__y_coordinates) >= 0:
            self.turn("NS", x_coordinates, y_coordinates)
        else:
            self.move(x_coordinates, y_coordinates)


    # Move or turn Gman until he reaches the target and return the remaining power
    def go_to_target(self, x_coordinates, y_coordinates):
        while not self.is_on_target(x_coordinates, y_coordinates):
            self.turn_or_move(x_coordinates, y_coordinates)

        return self.__power
