from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)

@app.route('/')
def guess_number():
    return ("<h1>Guess a number between 0 and 9</h1><img src='https://media.giphy.com/media/YqjFW9dzPW3O61gptq/giphy.gif'>")


@app.route("/<int:user_input>")
def check_number(user_input):
    colors = ["red", "purple", "blue", "grey", "brown", "black"]
    random_color = random.choice(colors)
    if user_input > random_number:
        return (f"<h1 style='color:{random_color}'>Too high, try again!</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    elif user_input < random_number:
        return (f'<h1 style="color:{random_color}">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    elif user_input == random_number:
        return ('<h1 style="color:green">You found me!</h1>'
                '<img src ="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')


if __name__ == "__main__":
    app.run(debug=True)