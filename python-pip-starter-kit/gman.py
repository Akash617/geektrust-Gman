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


    def which_way_to_turn(self, opposite, delta_x, delta_y):
        if opposite == "EW":
            if delta_y < 0:
                return "S"
            else:
                return "N"
        elif opposite == "NS":
            if delta_x < 0:
                return "W"
            else:
                return "E"


    # Turn Gman 90 degrees to face a direction he needs to go
    def turn(self, opposite, delta_x, delta_y):
        self.__direction = self.which_way_to_turn(opposite, delta_x, delta_y)
        self.__power -= self.__cost_to_turn


    # Move the Gman by 1 step in the direction he's facing
    def move(self):
        direction_assocation = {"N": (0,1), "E": (1,0), "S": (0,-1), "W": (-1,0)}

        self.__x_coordinates += direction_assocation[self.__direction][0]
        self.__y_coordinates += direction_assocation[self.__direction][1]

        self.__power -= self.__cost_to_move


    # Decide if the Gman needs to turn or if he can move in the direction he's facing
    def turn_or_move(self, delta_x, delta_y):
        if self.__direction == "E" and delta_x <= 0:
            self.turn("EW", delta_x, delta_y)
        elif self.__direction == "W" and delta_x >= 0:
            self.turn("EW", delta_x, delta_y)
        elif self.__direction == "N" and delta_y <= 0:
            self.turn("NS", delta_x, delta_y)
        elif self.__direction == "S" and delta_y >= 0:
            self.turn("NS", delta_x, delta_y)
        else:
            self.move()


    # Move or turn Gman until he reaches the target and return the remaining power
    def go_to_target(self, x_coordinates, y_coordinates):
        while not self.is_on_target(x_coordinates, y_coordinates):
            delta_x = x_coordinates - self.__x_coordinates
            delta_y = y_coordinates - self.__y_coordinates
            self.turn_or_move(delta_x, delta_y)

        return self.__power
