import random
import os

def board():
    issue : list = []
    for i in range(0, 4):
        issue.append([0] * 4)
    return issue

def randomShots(issue):
    for i in range(2):
        valueRandom: int = random.randint(0,9)
        if valueRandom > 0:
            value: int = 2
        else:
            value: int = 4
        i : int = random.randint(0,3)
        j : int = random.randint(0,3)
        issue[i][j] = value

def displayBoard(issue):
    for row in issue:
        print(row)

def move(issue):
    n: int = 0
    k: int = 1
    button: str = None
    while button not in ["Q", "D", "S", "Z"]:
        button = input("left: Q / right: D / down: S / up: Z \n").upper()
    for i in range(3):
        if button == "D":
            while issue[n + k] == 0 and n + k < 3:
                k += 1
            issue[n + k] = issue[n]
            issue[n] = 0
           
        elif button == "Q":
            while issue[n - k] == 0 and n + k > -1:
                k += 1
            issue[n - k] = issue[n]
            issue[n] = 0

def game():
    endGame: bool = False
    while endGame == False:
        os.system("cls")
        myBoard = board()
        randomShots(myBoard)
        displayBoard(myBoard)
        move()


game()