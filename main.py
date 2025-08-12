import math
import random

AI = "X"
HUMAN = "O"

template = [["","",""],
            ["","",""],
            ["","",""]]

testGrid = [["X","X","O"],
            ["","X",""],
            ["O","O","X"]]

# Check if AI or Human Won:
def whoWon(grid, row, column):
    if grid[row][column] == AI:
        return 1
    elif grid[row][column] == HUMAN:
        return -1
    
# Check for win
def winCheck(grid):
    # win (1), lose (-1), draw (0), still in progress = None

    # check columns (iterate 3 times)
    # return 1 or -1
    for column in range(0,3):
        if grid[0][column] == grid[1][column] == grid[2][column] != "":
            return whoWon(grid, 0, column)
            
    # check rows (iterate 3 times)
    # return 1 or -1
    for row in range(0,3):
        if grid[row][0] == grid[row][1] == grid[row][2] != "":
            return whoWon(grid, row, 0)
        
    # check diagonals (twice)
    # return 1 or -1
    # left corner:
    if grid[0][0] == grid[1][1] == grid[2][2] != "":
        return whoWon(grid, 1, 1)
    if grid[0][2] == grid[1][1] == grid[2][0] != "":
        return whoWon(grid, 1, 1)

    # draw if all spaces are full
    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
        return 0
    
    return None

# Find best move
def findBestMove():
    # best score = -infinity
    # best spaces = []
    # iterate through empty spaces
    # call minimax, if greater than best score, best spaces = [move]. if == best score, bestspaces.append(move)
    # if minimax is negative, you lost
    # if you've lost, keep playing? choose smallest depth? or biggest....
    
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
    # (pass a copy of the board, but in future maybe pass real board and then undo? for memory)
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

if __name__ == '__main__':
    print(winCheck(testGrid))