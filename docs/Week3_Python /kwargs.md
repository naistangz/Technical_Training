# Variable-length arguments (*args, **kwargs) in Python 

In Python, by adding `*` and `**` (one or two asterisks) to the head of parameter names in the function definition, you can specify an arbitrary number of arguments (variable-length arguments) when calling the function.

By convention, the names `*args`(arguments) and `**kwargs` (keyword arguments) are often used, but as long as `*` and `**` are headed, there are no problems with other names. 

* `*args` Receive multiple arguments as a tuple
* `**kwargs` Receive multiple keyword arguments as a dictionary

**Using `*args`**

```python 
def my_sum(*args):
    return sum(args)

print(my_sum(1, 2, 3, 4))
# Returns 10

print(my_sum(1, 2, 3, 4, 5, 6, 7, 8))
# Returns 36
``` 

You can also combine with positional arguments 

```python 
def the_sum(*args):
    print('args: ', args)
    print('type: ', type(args))
    print('sum: ', sum(args))

the_sum(1, 2, 3, 4)
# Returns 
# args: (1, 2, 3, 4)
# type: <class 'tuple'>
# sum: 10
```

**`**kwargs` Receive multiple keyword arguments as a dictionary**

The function can receive any number of keyword arguments. In the function, multiple keyword arguments are received as a dictionary whose `key` is argument name and whose `value` is value.

```python 
def func_kwargs(**kwargs):
    print('kwargs: ', kwargs)
    print('type: ', type(kwargs))

func_kwargs(key1=1, key2=2, key3=3)
# kwargs: {'key1': 1, 'key2': 2, 'key3':3}
# type: <class 'dict'>
``` 

A parameter with `**` can only be defined at last of the parameter list. If you define another parameter after the parameter with `**`, `SyntaxError` will occur. 

```python 
def func_kwargs_error(**kwargs, arg):
    print(kwargs)

# SyntaxError: invalid syntax
```

> `*args` exercise [HERE](function.py)