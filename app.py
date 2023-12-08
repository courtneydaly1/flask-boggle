from flask import Flask, request, render_template, session, jsonify
from boggle import Boggle

boggle_game = Boggle()
app = Flask(__name__)
app.config['SECRET_KEY']= "shhhhItsASecret"


@app.route("/")
def home():
    "show the board on the homepage"
    board = boggle_game.make_board()
    session['board']= board
    highscore= session.get("highscore", 0)
    num_plays = session.get("num_plays", 0)

    return render_template("index.html", board=board,highscore=highscore,num_plays=num_plays)

@app.route('/check_word')
def check_word():
    "check to see if the word is in the given dictionary"
    word= request.args["word"]
    board= session["board"]
    res= boggle_game.check_valid_word(board, word)

    return jsonify({'result': res})

@app.route('/post_score', methods=['POST'])
def post_score():
    """receive score, update num_plays, and update highscore"""
    score= request.json["score"]
    highscore=session.get('highscore',0)
    num_plays= session.get["num_plays", 0]

    session["num_plays"]= num_plays +1
    session['highscore']= max(score, highscore)

    return jsonify(newHighScore= score > highscore)












