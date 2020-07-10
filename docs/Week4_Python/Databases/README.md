# Using Databases with Python 


Importing `pyodbc` module
 
```bash
import pyodbc
```

Importing `pyodbc` module on MacOS

```bash
brew install unixodbc
```

## What is pyodbc?
- An open source Python module that eases access to ODBC databases. An OCBC driver uses the open database connectivity interface by Microsoft.


## Cursor 
- A control structure to allow the managing of rows of data from a response. The pyodbc instance is used to manage our queries directly with the database.

## Setting environment variables in PyCharm 

```python
import os
```

1. Open Run Configuration selector in top-right and click `Edit Configurations`
<img src="https://i.stack.imgur.com/4sPV0.jpg" alt="Run_configuration_pycharm">

2. Find `environmental variables` and click `PYTHONUNBUFFERED=1`
<img src="https://i.stack.imgur.com/IstkF.jpg" alt="Environment_variables">

3. Add or change variables, then click `OK` e.g Database, Password, etc
<img src="https://i.stack.imgur.com/l3ZRt.jpg alt="changing variables">

4. Restart interpreter

**Accessing environmental variables**
```python
import os 
print(os.environ.get('SOME_VAR'))
```
