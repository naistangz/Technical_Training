from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
from werkzeug.utils import secure_filename

# name of the module that is currently running in flask
app = Flask(__name__)
app.secret_key = 'h42314trge435rtgfdew345rt'

# print(__name__)

# home page
@app.route('/')
def home():
    return render_template('home.html')

# about page
@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        urls = {}
        # checking there are no duplicates
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)

        if request.form['code'] in urls.keys():
            flash('That short name has already been taken. Please select another name.')
            return redirect(url_for('home'))

        # checking if user has sent us a URL or whether they've sent a file
        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url':request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save('/Users/anaistang/DevOps_Training/docs/Week6_FlaskPython/url-shortener' + full_name)
            urls[request.form['code']] = {'file':full_name}

        # saving data onto a json file
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))


@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])




