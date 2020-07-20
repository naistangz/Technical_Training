from flask import Flask

# name of the module that is currently running in flask
app = Flask(__name__)

# print(__name__)


# home page
@app.route('/')
def home():
    return 'Hello Flask!'

# about page
@app.route('/about')
def about():
    return 'This is a url shortener'