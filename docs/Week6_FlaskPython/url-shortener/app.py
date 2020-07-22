from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify
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
    # we provide different codes that come as part of the cookies
    return render_template('home.html', codes=session.keys())

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
            f.save('/Users/anaistang/DevOps_Training/docs/Week6_FlaskPython/url-shortener/static/user_files/' + full_name)
            urls[request.form['code']] = {'file':full_name}

        # saving data onto a json file
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
            # saving data into a cookie
            session[request.form['code']] = True
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
                else:
                    # search for a static file
                    return redirect(url_for('static', filename='user_files/' + urls[code]['file']))
    return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404 # 404 error code

# cookies save information to user's browser
# keep me signed in uses cookies

# route for api
# creating an api
# jsonify takes any list or dictionary and takes it into json format
@app.route('/api')
def session_api():
    return jsonify(list(session.keys()))


# if python interpreter is running this module as the main program, it sets __name__ variable to have a value '__main__'
# Tells us whether the python module was executed as a script, or imported from another module. It will only enter if __name__ == __main__ block if file was executed as a script (main module)
if __name__ == "__main__":
    # to run in environment production
    app.run(debug=True)
