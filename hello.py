from flask import Flask
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