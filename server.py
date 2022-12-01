from flask import Flask
import random

app = Flask(__name__)
#
winning_number = random.randint(1, 10)

@app.route('/')
def homepage():
    return '<h1> Guess a number between 0 & 9</h1> ' \
           '<iframe src="https://giphy.com/embed/l378khQxt68syiWJy" width="400" height="400"> '


@app.route('/<number>')
def check_answer(number):
    if int(number) == winning_number:
        return "<h1 style='color: green'>That is correct answer. You Won!</h1>" \
               "<iframe src='https://giphy.com/embed/3o6UB3VhArvomJHtdK' width='400' height='400'>"

    elif int(number) > winning_number:
        return "<h1 style='color: red'>Too high, Try again!</h1> " \
               "<iframe src='https://giphy.com/embed/t9l9L8qFKJfsFn2WLm' width='400' height='400'> "

    elif int(number) < winning_number:
        return "<h1 style='color: purple'>Too Low, Try Again!</h1>" \
               " <iframe src='https://giphy.com/embed/TgmiJ4AZ3HSiIqpOj6' width='400' height='400'> "

app.run(debug=True)
