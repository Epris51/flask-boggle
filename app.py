from flask import Flask, request, jsonify
from boggle import Boggle

app = Flask(__name__)

# Create an instance of the Boggle game
boggle_game = Boggle()

@app.route('/new-game')
def new_game():
    """Create a new game and return the board."""
    board = boggle_game.make_board()
    return jsonify(board=board)

@app.route('/guess', methods=['POST'])
def guess():
    """Accept a guess and check if it's valid."""
    data = request.get_json()
    word = data.get('word', '')
    board = data.get('board', [])

    result = boggle_game.check_valid_word(board, word)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)


