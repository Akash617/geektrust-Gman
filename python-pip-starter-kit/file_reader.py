import file_handler

class File_reader():
    def __init__(self, file):
        self.__file = file
        self.__remaining_power = 200


    def read_file(self):
        self.__lines = self.__file.readlines()

        self.file_handler = file_handler.File_handler()
        self.file_handler.handle(self.__lines)
