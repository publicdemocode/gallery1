from flask import Flask, render_template

app = Flask(__name__)

@app.route("/show_user/<int:user_id>")
def show_user(user_id):
    
    #out = "<div style='font-size: 18'>User name: {0} <br> Live in: {1} <br> Like: {2} <br> Favirites: {3}</div>" . format(name, city, food, favorites)
    #return out

    user_data = get_user_data(user_id)

    return render_template('show_user.html', user_data = user_data)


def get_user_data(user_id):

    if user_id == 1:
        user_data = {
            "user_id" : 1,
            "name" : "alexey",
            "city" : "Petah Tikva",  
            "user_food" : "salad",
            "user_favorites" : "Travelling, Cookking, Playing football",
            "tel" : "058",
            "color" : "green"
        }

    if user_id == 2:
        user_data = {
            "user_id" : 2,
            "name" : "Victor",
            "city" : "Ashkelon",  
            "user_food" : "salad",
            "user_favorites" : "Travelling, Cookking, Playing football",
            "tel" : "052",
            "color" : "green"
        }

    return user_data


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello/<username>')
def abc(username):
    return "Hello " + username


@app.route('/greet/<timing>/<username>')
def greet(timing,username):
    return "Good  " + str(timing) + " " + str(username)



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