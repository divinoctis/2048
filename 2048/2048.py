import random
import os

def board():
    grid : list = []
    for i in range(0, 4):
        grid.append([0] * 4)
    return grid

def randomShots(grid):
    for i in range(2):
        valueRandom: int = random.randint(0,9)
        if valueRandom > 0:
            value: int = 2
        else:
            value: int = 4
        i : int = random.randint(0,3)
        j : int = random.randint(0,3)
        grid[i][j] = value

def displayBoard(grid):
    for row in grid:
        print(row)
        
'''
def merge():
    

def move_left(grid):
    

    pass
'''

def move(grid):
    n: int = 0
    k: int = 1
    button: str = None
    while button not in ["Q", "D", "S", "Z"]:
        button = input("left: Q / right: D / down: S / up: Z \n").upper()
    while i < len(grid):
        if button == "D":
            while grid[i][n + k] == 0 and n + k < 3:
                k += 1
            grid[n][n + k] = grid[i][n]
            grid[n][n] = 0

        elif button == "Q":
            while grid[n - k] == 0 and n + k > -1:
                k += 1
            grid[n - k] = grid[n]
            grid[n] = 0

        elif button == "Z":
            while grid[n - k] == 0 and n + k > -1:
                k += 1
            grid[n - k] = grid[n]
            grid[n] = 0
            
        elif button == "S":
            while grid[n - k] == 0 and n + k > -1:
                k += 1
            grid[n - k] = grid[n]
            grid[n] = 0
        i +=1

def game():
    endGame = False
    while not endGame:
        os.system("cls")
        myBoard = board()
        randomShots(myBoard)
        displayBoard(myBoard)
        move(myBoard)

game()