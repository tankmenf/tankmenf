from flask import Flask, render_template
import random
import string

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route("/привет")
def hi_world():
    return '<h1>привет<h1>'

@app.route("/green")
def green_world():
    list =["растения зелёные", "растения нужно поливать", "растениям нужен свет"]
    return f'<h1>{random.choice(list)}<h1>'

@app.route("/chees")
def farfar():
    return render_template('index.html')

@app.route("/<size>")
def darada(size):
    print(size)
    return render_template('index.html',sitt=size)

@app.route("/opel")
def money():
    money = ["Орёл", "Решка" ]
    return f'<h1>{random.choice(money)}<h1>'

@app.route("/foto")
def Photo():
    pictures = ["2.jpg", "кот.jpg", "собака.jpg"]
    return f'<h1>{random.choice(pictures)}<h1>'

@app.route('/gen_pass/<int:pass_length>')
def gen_pass(pass_length):
    """Generates a random password of a specified length."""
    elements = string.ascii_letters + string.digits
    password = ''.join(random.choice(elements) for _ in range(pass_length))
    return password

if __name__ == '__main__':


    app.run(debug=True)