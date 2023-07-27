import gman

class File_reader():
    def __init__(self, file):
        self.__file = file
        self.__remaining_power = 200


    def read_file(self):
        self.__lines = self.__file.readlines()

        for self.__line in self.__lines:
            # Format lines, remove the newline and split into a list
            self.__line = self.__line.replace("\n", "").split(" ")

            if self.__line[0] == "SOURCE":
                g_man = gman.Gman(int(self.__line[1]), int(self.__line[2]), self.__line[3])
            elif self.__line[0] == "DESTINATION":
                self.__remaining_power = g_man.go_to(int(self.__line[1]), int(self.__line[2]))
            elif self.__line[0] == "PRINT_POWER":
                print("POWER " + str(self.__remaining_power))