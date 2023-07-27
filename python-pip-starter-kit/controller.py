import gman

class Controller:
    def __init__(self):
        pass

    def handle(self, lines):
        # Iterate over lines in the file
        for self.__line in lines:
            # Format lines, remove the newline and split into a list
            self.__line = self.__line.replace("\n", "").split(" ")

            # Create a Gman class at the source point
            if self.__line[0] == "SOURCE":
                gman_instance = gman.Gman(int(self.__line[1]), int(self.__line[2]), self.__line[3])
            elif self.__line[0] == "DESTINATION":
                self.__remaining_power = gman_instance.go_to_target(int(self.__line[1]), int(self.__line[2]))
            elif self.__line[0] == "PRINT_POWER":
                print("POWER " + str(self.__remaining_power))