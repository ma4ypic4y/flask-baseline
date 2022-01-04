from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(1+2)
    return 'Hello, d'
