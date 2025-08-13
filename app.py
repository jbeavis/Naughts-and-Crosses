from flask import Flask, render_template, request, jsonify
import math
import random
import game

app = Flask(__name__)

# game.game()
grid = game.template

@app.route("/")
def index():
    return render_template("index.html", grid=grid)

@app.route("/play", methods=["POST"])
def play():
    global grid
    data = request.json
    row, col = data["row"], data["col"]

    # Player move
    if grid[row][col] == "":
        grid[row][col] = game.HUMAN # Human symbol
    elif game.winCheck(grid) is not None:
        return jsonify({"error": "Game over"}), 400
    else:
        return jsonify({"error": "Invalid move"}), 400

    # Check if player won
    if game.winCheck(grid) is not None:
        return jsonify({"grid": grid, "winner": game.winCheck(grid)})

    # AI move
    ai_row, ai_col = game.findBestMove(grid)
    grid[ai_row][ai_col] = game.AI

    return jsonify({"grid": grid, "winner": game.winCheck(grid)})

@app.route("/reset", methods=["POST"])
def reset():
    global grid
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            grid[row][column] = ""
    return jsonify({"grid": grid})