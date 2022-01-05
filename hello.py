from flask import Flask, request, jsonify, abort, redirect, url_for, render_template, send_file
import joblib
import numpy as np


app = Flask(__name__)


knn = joblib.load('knn.pkl')

@app.route('/')
def hello_world():
    print(1+2)
    return 'Hello, d'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers),1)


@app.route('/avg/<nums>')
def avg(nums):
    nums= nums.split(',')
    nums= [float(num) for num in nums]
    num_mean = np.mean(nums)
    print(f'{num_mean}')

    return str(num_mean)



@app.route('/iris/<param>')
def iris(param):
    param= param.split(',')
    param= [float(num) for num in param]
    param = np.array(param).reshape(1,-1)
    predict = knn.predict(param) 

    return str(predict)

@app.route('/show_image')
def show_image():
    return '<img src="./static/setosa.jpg" alt="setosa">'


@app.route('/badrequest400')
def bad_request():
    return abort(400)

# POST query
@app.route('/iris_post', methods=['POST'])
def add_message():
    try:
        content = request.get_json()
        print(content)
        param = content['flower'].split(',')
        param = [float(num) for num in param]
    
        param = np.array(param).reshape(1, -1)
        predict = knn.predict(param)

        predict = {'class':str(predict[0])}
    except:
        return redirect(url_for('bad_request'))

    return jsonify(predict)



from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    file = FileField()

from werkzeug.utils import secure_filename
import os

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)
