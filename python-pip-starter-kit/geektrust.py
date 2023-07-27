from sys import argv
import file_reader


def main():

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')

    file = file_reader.File_reader(f)
    file.read_file()

    
if __name__ == "__main__":
    main()