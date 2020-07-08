# File Handling in Python

In python, it is not necessary to import external libraries to read and write files. 
Python provides an inbuilt function for creating, writing and reading files. 

## Opening a text file 

Syntax
```python
file_object = open("filename", "mode")
```

**Filename:** Gives name of the file that file object has opened.
**Mode:** Attribute of a file object you which mode used to open a file.

## Creating a text file
Syntax

```python
file = open("filetext.txt"w+")
```

- We have declared the variable file to open a file named `"filetext.txt"`. Open takes 2 arguments the file that we want to open and a string that represents the kinds of permission or operation we want to do on the file.
- "w" indicates write and creates a file if it does not exit in the library.
- "w+" indicates read and write

```python
for i in range(5):
    f.write("This is line %d\r\n" % (i+1))
```

- For loop runs over a range of 5 numbers
- Using **write** function to enter data into the file
- The output we iterate in the file is "this is line {number}", which we declare with "w" function and %d which displays the integer

**Output:**
```text
filetext.txt

This is line 1

This is line 2

This is line 3

This is line 4

This is line 5
```

**Closing the file:**

It is good practice to close files 

```python
f.close()
```
- Closes instance of the file `"filetext.txt"`

## Appending data to a file 

Syntax 
```python
f = open("filetext.txt", "a+")
```
`a+` indicates that it will read and append new data onto the file.

**Appending new data:**
```python
for i in range(2):
    f.write("Appended line %d\r\n" % (i+1))

# closing the file
f.close()
```
**Output:**
```text
filetext.txt

This is line 1

This is line 2

This is line 3

This is line 4

This is line 5

Appended line 1

Appended line 2
```

## Reading a file 

Syntax
```python
f = open("filetext.txt", "r")
    # Mode function to check that the file is in open mode. If yes, we proceed ahead
    if f.mode == "r":
    
    # Using f.read() to read file data and store it in the variable content
    content= f.read()
```

**Output:**

```text
filetext.txt

This is line 1

This is line 2

This is line 3

This is line 4

This is line 5
```

## Reading a file line by line 

If your data is too big to read, `readlines()` code will segregate your data in easy to read mode.

Syntax
```python
f1=f.readlines()
```
This will read the file or document line by line and separate each line and present the file in a readable format

## File Modes in Python 

**Mode**|**Description**
-----|------
'r'|This is default mode, opens file for reading
'w'|Opens file for writing. If file does not exist, it creates a new file. If file exists, it truncates the file.
'x'|Creates new file, it file already exists, operation fails.
'a'| Opens files in append mode. If file does not exist, it creates a new file
't'| Default mode, opens in text mode
'b'| Opens in binary mode 
'+'|Opens file for reading and writing(updating)

## Python Check if File or Directory Exists using built-in library functions

The builtin `OS` module in python provides functions for interacting with the operating system

**Importing os.path module:**

```python
import os.path
from os import path
```

Using the `path.exists()` function to check whether a File exists.

```python
path.exists("filetext.txt") # Returns boolean
```

**`OS` Module**| Output
----|-----
`os.path.exists()`| Returns `True` if path or directory exists
`os.path.isfile()`| Returns `True` if path is File
`os.path.isdir()`| Returns `True` if path is Directory
`pathlib.Path.exists()`|Returns `True` if path or directory does exist

## Renaming Files and Directories using `os.rename()`

`rename()` method is used to rename a file or directoy. It takes two arguments.

Syntax:
```python
os.rename(src, dst)
```

**src:** Source is name of file or directory. It should already exists

**dst:** Destination is the new name of the file or directory you want to change.

> Handling Errors in files
>
>[Error Handling](text_file1_error_handling.py)
>
>[Main.py](main1_error_handling.py)