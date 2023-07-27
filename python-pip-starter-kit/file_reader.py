import controller

class File_reader():
    def __init__(self, file):
        self.__file = file
        self.__remaining_power = 200


    def read_file(self):
        self.__lines = self.__file.readlines()

        self.__controller = controller.Controller()
        self.__controller.handle(self.__lines)
