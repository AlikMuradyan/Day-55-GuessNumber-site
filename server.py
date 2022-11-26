from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)

@app.route('/')
def hello_world():
    return "<h1 style='color: green'>Guess a number between 0 and 9</h1>"\
           "<img src='https://media.giphy.com/media/xUn3CftPBajoflzROU/giphy-downsized-large.gif'>"

@app.route('/<int:number>')
def check_the_answer(number):
    print(random_number)
    if number < random_number:
        return "<h1 style='color: green'>Too low, try again!</h1>""<img src='https://media.giphy.com/media/0E6nXSLFtqcPKs8trF/giphy.gif'>"

    elif number > random_number:
        return "<h1 style='color: green'>Too high, try again!</h1>""<img src='https://media.giphy.com/media/mvYy4JcOK9IWWLN9Zg/giphy.gif'>"
    else:
        return "<h1 style='color: green'>You found it!</h1>""<img src='https://media.giphy.com/media/YRuFixSNWFVcXaxpmX/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)