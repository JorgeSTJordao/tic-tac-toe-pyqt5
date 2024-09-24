from flask import Flask, render_template, url_for
from config import url
from domain.Play import Play

app = Flask(__name__, template_folder='templates')

player = Play(url)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/play")
def play():

    player.select_word()

    return render_template("play.html", word_selected=player.word_selected)


if __name__ == '__main__':
    app.run(debug=True)
