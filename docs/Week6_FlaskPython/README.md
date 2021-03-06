# Flask :snake:

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

If you already have a process bound to the default port (5000), locate the process:
```bash
$ ps -fA | grep python
```

```bash
501 81651 12648 0 9:53PM ttys000 0:00.00 grep python
```

Stop the server by sending it a signal (the second number - process number)
```bash
kill 81651
```

**or:**

Run the server on a *different** port, by specifying the alternative port on the command line:
```bash
$ python -m SimpleHTTPServer 8910
Serving HTTP on 0.0.0.0 port 8910
```

Then access the server as `http://localhost:8910`; where `8910` can be any number from 1024 and up, provided the port is not already taken.



## Pros and Cons of Flask 

**Pros**|**Cons**
----|----
Easy to get started | Extremely limited, you have to build almost everything that you want to do in Flask
Very customisable | No database support, you have to write all your custom SQL statements and create objects and turn them back into database data.
Web Server Gateway Interface (WSGI) compatible |


## Terminology 

**Model View Controller (MVC)**
- A software design pattern used for developing user interfaces that divides the related program logic into three interconnected elements, **Model,** **View** and **Controller.**
- The **MVC** model or 'pattern' is used for developing modern user interfaces.
- Each architecture component is built to handle specific development aspect of an application 
- MVC separates the business logic and presentation layer from each other. 

<img src="https://www.guru99.com/images/1/122118_0445_MVCTutorial1.png" alt="mvc_image">


- **Model** - Includes all data and its related logic (a way for talking about data)
- **View** - Presents data and its related logic (a way for talking about user interfaces) MVC is HTML, CSS and some special syntax.
- **Controller** - An interface between Model and View components (a way for talking about program logic) aka the request handler

When a user enters a URL in the browser, it goes to the webserver and routed to a controller. A controller executes related view and models for that request and creates the response and sends it back to the browser.

**Flask MVC Structure:**
What?
- A popular architecture for designing applications that have a user interface
- MVC is a collection of software design patterns that provide a vocabulary for designing your application. 


---
**End Point**
- Any device that is physically an end point on a network
- One end of a communication channel

---

**WSGI (Web Server Gateway Interface)**
Frameworks|Servers
------|------
Flask | Gunicorn
Django| uWSGI

- WSGI is a protocol for Python applications in order to serve websites in a uniform manner.
- Examples of Python frameworks include Flask or Django
- Examples of servers include Gunicorn and uWSGI
- If we have a Python framework that wants to serve webpages, if it follows the WSGI format, that means that any Python framework you choose can work with any compatible WSGI server. 
- Flask and Django by default implement those, same as Gunicorn and uWSGI

# Flask Projects
- [URL Shortener](url-shortener)
- [Flask Authorisation App](https://github.com/naistangz/flask_autho_app/tree/master/flask_autho_app)