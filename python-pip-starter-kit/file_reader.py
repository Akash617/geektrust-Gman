import gman

class File_reader():
    def __init__(self):
        self.__remaining_power = 200


    def read_file(self, file):
        self.__lines = self.__file.readlines()

        for self.__line in self.__lines:
            # Format lines, remove the newline and split into a list
            self.__line = self.__line.replace("\n", "").split(" ")

            if self.__line[0] == "SOURCE":
                gman = gman.Gman(self.__line[1], self.__line[2], self.__line[3])
            elif self.__line[0] == "DESTINATION":
                self.__remaining_power = gman.go_to(self.__line[1], self.__line[2])
            elif self.__line[0] == "PRINT_POWER":
                print(self.__remaining_power)
