class TextFileHandlingError:

    def __init__(self, file_path, text_storage=None):
        # Initialising attributes
        self.file_path = file_path
        self.text_storage = text_storage

    def readTextFile(self):

        # Execute the following code which may raise an exception
        try:
            f = open(self.file_path, "r")

        # If there is no exception, only try clause will run
        # If any exception occurred, try clause will be skipped and else clause will run
        # except will capture the thrown exception
        # Aliasing exception as e
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
        # If exception is not thrown, program will run the following code
        else:
            print(f.read())

            # reading lines
            self.text_storage = f.readline()
            self.text_storage = f.readlines()
            # self.text_storage=file.read(3) # Reads first 3 characters in the text file

            # The pointer is at the current position and will start reading from there
            print(f.tell())

            # Tells the pointer to go back at that particular position mentioned.
            f.seek(0)

            # closing the file when done
            # file.close() # Good practice to close files as python has a limit on the number of files that can be open
            f.close()
            return self.text_storage

    def playWithExceptions(self):

        try:
            f = open(self.file_path, 'r')

        # aliasing error as e
        # Optional block
        # Handling of exception (if required)
        except Exception as e:
            print(e)
            print("The file does not exist")
        else:
            print("I am in the else clause")
            self.text_storage = f.readline()
            f.close()

        # Finally defines block of code to run when try...except..else block is final
        # Finally block executes no matter if the try block raises an error or not (always executed)
        finally:
            print("Read line method successful")
            return self.text_storage

    def raiseException(self):
            try:
                name = str(input("Enter your name:\n"))
                if len(name) == 0:
                    raise Exception
            except Exception:
                print("You have not entered your name. Please try again")
                self.raiseException()
            else:
                print(f"Welcome! {name}")
