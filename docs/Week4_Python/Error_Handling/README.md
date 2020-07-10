# Error Handling :exclamation: :boom:

Homework:
> - [URL Error](urllib_error.py)
>   - [errorlog.txt](errorlog.txt)
>   - [errorHTTPlog.txt](errorHTTPlog.txt)
>   - [successfulHTTP.txt](successfulHTTP.txt)

Reading images using the pillow module:
> - [Image_Reader](read_image.py)


## Exceptions 
- Errors that occur during execution of a program. When that error occurs, Python generates an exception that can be handled, which avoids the program to crash

# Raising an exception 
Raising an exception using the raise exception statement

## Common exception errors 

Exception Errors| Explanation 
-----|--------
IOError| If the file cannot be opened
ImportError|If python cannot find the module 
ValueError|Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value e.g. printing `int` instead of `str`
KeyboardInterrupt|Raised when user hits the interrupt key 
EOFError|Raised when one of the built-in functions `input()` or `raw_input()` hits an end-of-file condition (EOF) without reading any data
NameError|Raised when Py interpreter does not recognise a local or global object name 

**NameError Example:**
```python 
>>> print 10 * ten
Traceback (most recent call last):
  File "", line 1, in 
NameError: name 'ten' is not defined

and this output show it's a TypeError
>>> print 1 + 'ten'
Traceback (most recent call last):
  File "", line 1, in 
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

**Try and Except**
```python 
# code that may raise an error
try:
    fh = open("non_existing_file")

# code that should run if the code inside the try block fails
# Input/Output Error
except IOError:
    print("The file does not exist")
```

**Handling ValueErrors**
```python

while True:
try:
    x = int(raw_input("Please enter a number:))
    break
except ValueError:
    print("That was not a valid number")
```

**Or:**
```python 
import sys
print "Lets fix the previous code with exception handling"

try:
number = int(raw_input("Enter a number between 1 - 10"))

except ValueError:
print "Err.. numbers only"
sys.exit()

print "you entered number", number
```