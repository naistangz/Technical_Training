# Flask 

# What is flask?
- A micro web framework written in Python 
- It is called microframework because it does not require particular tools or libraries.
- It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.
- Allows developers to build web applications easily 
- A lightweight WSGI web application framework


:bulb: Developed by Armin Ronacher, who led team of international Python enthusiasts called Poocco :bulb:

# What is a web framework?
- Represents a collection of libraries and modules that enable web application developers to write applications without worrying about low-level details such as protocol, thread management, etc.

# What is a micro framework?
- Refers to minimalistic web application frameworks
- Lacks most functionality which is common to expect in full-fledged web application framework (accounts, authentication, authorisation, etc)


Boilerplate code example
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

Running flask in dev environment 
```bash
bash-3.2$ export FLASK_ENV=development 
bash-3.2$ flask run
 * Serving Flask app "hello" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 891-424-380
```
## Pros and Cons of Flask 

**Pros**|**Cons**
----|----
Easy to get started | Extremely limited, you have to build almost everything that you want to do in Flask
Very customisable | No database support, you have to write all your custom SQL statements and create objects and turn them back into database data.
Web Server Gateway Interface (WSGI) compatible |

## **Mini flask project**
- [URL Shortener](url-shortener)