import math
import random

AI = "X"
HUMAN = "O"

testGrid = [["","",""],
            ["","",""],
            ["","",""]]

# Check for win
def winCheck():
    # win (1), lose (-1), draw (o), still in progress = "None"
    # draw if all spaces are full
    return

# Find best move
def findBestMove():
    # start list of possible win spaces, empty 
    # start list of possible draw spaces, empty
    # iterate through empty spaces
    # call minimax, if positive or a draw, add space to respective list
    # if minimax is negative, you lost
    
    # pick random space from list of possible spaces, starting with win list if not empty, then moving on to draw spaces
    # place x on board 
    return

# Minimax
def minimax(board, isMaximising): #later add depth
    # ismaximising means it's the ai turn, else simulate the player
    # check for win state, return if there is one

    # if currently nothing, continue and... 

    # if maximising, 
    # best score = -infinity
    # iterate through empty squares
    # call minimaxing(ismaximising = false)
    # if higher than best score, update var
    # when finished, return best score

    # if not maximising,
    # best score = +infinity
    # iterate through empty squares
    # call minimaxing(ismaximising = true)
    # if lower than best score, update var
    # when finished, return best score

    return #best score

# later add alpha beta pruning