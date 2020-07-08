class TextFileHandling:

    def __init__(self, file_path, text_storage=None):
        # Initialising attributes
        self.file_path = file_path
        self.text_storage = text_storage

    # Reading the file in two ways
    def readTextFile(self):

        # Opening the file for appending text to the end
        # file = open(self.file_path, "a")

        # Open the file with read access
        file = open(self.file_path, "r")

        # self.text_storage = file.read()
        print(file.read(1))

        # reading lines
        self.text_storage = file.readline()
        self.text_storage = file.readlines()

        # The pointer is at the current position and will start reading from there
        print(file.tell())

        # Tells the pointer to go back at that particular position mentioned.
        file.seek(0)
        # for line in file:
        #     print(line)

        # closing the file when done
        file.close()
        # self.text_storage=file.read(3) # Reads first 3 characters in the text file
        # file.close() # Good practice to close files as python has a limit on the number of files that can be open
        return self.text_storage

    def writeTextFile(self):

        # Opening a file or writing and creating it if it doesn't exist w+
        file = open("writer.txt", "w")

        # Writing a file
        file.write("My first file using python")
        file.close()

        # Overriding the file
        # file.write("I am overriding the file")
        # file.close()

        # Appending the file with additional text instead of overriding
        file = open("writer.txt", "a+")
        file.write("\nNew line of text")

        # seek() sets the file's current position at the offset. Defaults to 0, 1 means current position, 2 means file's end
        # Reposition the file to 0 because we have reached the end of the file
        file.seek(0)

        # Reading the file after appending new text
        self.text_storage=file.read() # If file = open("writer.txt, "a"), this will return an error so a+ is required to read AND append
        file.close()

        # Status of closure
        print(file.closed) # True

        # Name of current file
        print(file.name) # writer.txt

        # Default mode is "r", prints out current access mode
        print(file.mode) # a+
        return self.text_storage

    def readTextFileUsingWith(self):

        # To reduce overhead of closing files
        # Open the file in read mode. No overhead of closing as it automatically closes the file.
        # Closes the file when an exception is raised
        with open("order2.txt", "r") as f:
            self.text_storage=f.read()
            return self.text_storage

    def writeTextFileUsingWith(self):
        # w+ write and read mode
        # will override the text NOT append
        with open("writer.txt", "w+") as f:
            f.write("Using writer with functionality")

            # The pointer is at the end, when returning, it will print none unless file.seek(0)
            # tell prints out current file position in a file stream
            print(f.tell())  # 31 byte

            # Repositioning pointer to the beginning because the pointer after f.write is at the end.
            f.seek(0)

            # Reading the file
            self.text_storage=f.read()
            return self.text_storage

    def playingWithPythonOSModule(self):
        # Provides functions for interacting with the operating system
        import os

        # Prints current working directory
        # Prints /Users/anaistang/DevOps_Training/docs/Week4_Python/File_Handling
        cwd_result = os.getcwd()
        print(cwd_result)

        # Removing "writer.txt" file
        # os.remove("writer.txt")

        # Listing the directory
        # Prints ['text_file1.py', '__pycache__', 'order.txt', 'README.md', 'text_file.py', 'order2.txt', 'main.py', 'main1.py']
        # print(os.listdir())

        # Renaming a file. Takes two args: first argument is file to modify, second argument is the modified name
        # os.rename('order2.txt', 'modified.txt')

        # Changing the directory
        # os.chdir("path name")
        os.chdir("/Users/anaistang/DevOps_Training/docs/Week4_Python/File_Handling")
        updated_cwd = os.getcwd()
        print(f"Directory changed successfully!\nCurrent directory: ", updated_cwd)

        # Creating a directory
        # Creates a new directory within my File_Handling directory
        # creating_dir = os.mkdir("New_directory")
        # print(f"A new directory has been created", creating_dir)

        # Removing a directory
        # Removes the directory from my File_Handling directory
        # removing_dir = os.rmdir("New_directory")
        # print(f"Directory has been deleted successfully")



