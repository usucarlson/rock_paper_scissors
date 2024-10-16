from flask import Flask
from flask import render_template
import random

app = Flask(__name__)
@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/rock")
def rock():
    com = random.randint(1,3)
    if com == 1:
        return render_template("rock-rock.html")
    if com == 2:
        return render_template("rock-paper.html")
    if com == 3:
        return render_template("rock-scissors.html")

@app.route("/paper")
def paper():
    com = random.randint(1,3)
    if com == 1:
        return render_template("paper-rock.html")
    if com == 2:
        return render_template("paper-paper.html")
    if com == 3:
        return render_template("paper-scissors.html")

@app.route("/scissors")
def scissors():
    com = random.randint(1,3)
    if com == 1:
        return render_template("scissors-rock.html")
    if com == 2:
        return render_template("scissors-paper.html")
    if com == 3:
        return render_template("scissors-scissors.html")
