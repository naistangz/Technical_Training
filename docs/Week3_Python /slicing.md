# Python slice()

The slice() function returns a slice object that can be used to slice strings, lists, tuples, etc.

The syntax of `slice()` is:
```python
slice(start, stop, step)
```

**slice() Parameters**
`slice()` can take three parameters:
* **start(optional)** - Starting integer where the slicing of the object starts. Default to `None` if not provided.
* **stop** - Integer until which the slicing takes place. The slicing stop at index **stop -1 (last element).**
* **step(optional)** - Integer value which determines the increment between each index for slicing. Default to `None` if not provided.

**Example 1: Create a slice object for slicing**
```python 
py_string = "Python"

# Slices 0, 1, 2 indices 
slice_object = slice(3)
print(py_string[slice_object]) # Returns Pyt

# Start = 1, stop = 6, step = 2
slice_object = slice(1, 6, 2)
print(py_string[slice_object]) #yhn

new_slice = py_string[1::2] # Also returns yhn
```

> Slicing and Indexing exercises [HERE](string_casting.py)
