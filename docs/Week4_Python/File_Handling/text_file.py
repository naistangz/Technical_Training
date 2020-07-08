class TextFileHandling:

    def __init__(self, file_path, text_storage=None):
        # Initialising attributes
        self.file_path = file_path
        self.text_storage = text_storage

    # Reading the file in two ways
    def readTextFile(self):
        # Open the file
        # Read the file
        # Closing the file
        file = open(self.file_path, "r")  # Read mode
        # self.text_storage = file.read()
        print(file.read(1))
        self.text_storage = file.readline()
        self.text_storage = file.readlines()
        print(file.tell())  # The pointer is at the current position and will start reading from there
        # for line in file:
        #     print(line)
        file.close()
        # self.text_storage=file.read(3) # Reads first 3 characters in the text file
        # file.close() # Good practice to close files as python has a limit on the number of files that can be open
        return self.text_storage

    def writeTextFile(self):
        pass

    def readTextFileUsingWith(self):
        pass

    def writeTextFileUsingWith(self):
        pass
