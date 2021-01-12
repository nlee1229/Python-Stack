
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def md_board():
    return render_template('index.html', board_height = 8, board_width = 8)

@app.route('/4')
def sm_board():
    return render_template('index.html', board_height = 8, board_width = 4)

@app.route('/<int:x>/<int:y>')
def any_board(x, y):
    return render_template('index.html', board_height = x, board_width = y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def any_board2(x, y, color1, color2):
    return render_template('index.html', board_height = x, board_width = y, check_color1 = color1, check_color2 = color2)

if __name__ == "__main__":
    app.run(debug=True)
