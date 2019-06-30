import wikipedia_game
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def form_post():
    text = request.form['text']
    link = 'https://en.wikipedia.org/' + text
    return wikipedia_game.run_bfs(link)
