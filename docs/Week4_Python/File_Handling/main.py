# Class Objectives
# 1. Reading from and writing to files
# 2. Exception Handling
# 3. CSV
# 4. Assignments
from text_file import TextFileHandling

file_path = 'order.txt'

textfileObject = TextFileHandling(file_path)

print(textfileObject.readTextFile()) # Prints order.txt