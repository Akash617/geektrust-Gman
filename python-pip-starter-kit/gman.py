class Gman():
    def __init__(self, x, y, direction):
        self.__x = x
        self.__y = y
        self.__direction = direction
        self.__power = 200
        self.__cost_to_turn = 5
        self.__cost_to_move = 10


    # Check if Gman is on target or not
    def on_target(self, x, y):
        if self.__x != x or self.__y != y:
            return False

        return True


    # Turn Gman 90 degrees to face a direction he needs to go
    def turn(self, opposite, x, y):
        if opposite == "EW":
            if (y - self.__y) < 0:
                self.__direction = "S"
                self.__power -= self.__cost_to_turn
            else:
                self.__direction = "N"
                self.__power -= self.__cost_to_turn
        elif opposite == "NS":
            if (x - self.__x) < 0:
                self.__direction = "W"
                self.__power -= self.__cost_to_turn
            else:
                self.__direction = "E"
                self.__power -= self.__cost_to_turn


    # Move the Gman by 1 step in the direction he's facing
    def move(self, x, y):
        direction_assocation = {"N": (0,1), "E": (1,0), "S": (0,-1), "W": (-1,0)}

        self.__x += direction_assocation[self.__direction][0]
        self.__y += direction_assocation[self.__direction][1]

        self.__power -= self.__cost_to_move


    # Decide if the Gman needs to turn or if he can move in the direction he's facing
    def turn_or_move(self, x, y):
        if self.__direction == "E" and (x - self.__x) <= 0:
            self.turn("EW", x, y)
        elif self.__direction == "W" and (x - self.__x) >= 0:
            self.turn("EW", x, y)
        elif self.__direction == "N" and (y - self.__y) <= 0:
            self.turn("NS", x, y)
        elif self.__direction == "S" and (y - self.__y) >= 0:
            self.turn("NS", x, y)
        else:
            self.move(x, y)


    # Move or turn Gman until he reaches the target and return the remaining power
    def go_to(self, x, y):
        while not self.on_target(x, y):
            self.turn_or_move(x, y)

        return self.__power
