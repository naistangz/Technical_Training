from text_file1_error_handling import TextFileHandlingError

file_path = 'order.txt'

# Instantiating TextFileHandlingError object
textfileObject = TextFileHandlingError(file_path)

# Calling readTextFile method
textfileObject.readTextFile()

# Calling playWithExceptions method
# Prints Dumplings
print(textfileObject.playWithExceptions())

# Using raised exceptions
print(textfileObject.raiseException())