from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello/<username>')
def abc(username):
    return "Hello " + username


@app.route('/greet/<timing>/<username>')
def greet(timing,username):
    return "Good  " + timing + " " + username



@app.route("/alexey")
def hello_alexey():
    print("called hello Alexey2")
    return "<h3>Hello, Alexey2!</h3>"


@app.route("/victor")
def hello_victor():
    return "<h3>Hello, Victor</h3>"


@app.route("/user/add")
def add_user():
    return "User add logic"


if __name__ == "__main__":
    app.run('0.0.0.0', 3010, debug=True)


'''
pip3 install flask
python3 app.py

'''