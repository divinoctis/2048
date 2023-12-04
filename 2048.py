import random
import os

def board():
    issue: list[list[int]] = []
    for i in range(0, 3):
        issue.append([] * 4)

def randomShots(issue):
    rate: list[int] = [0,1,2,3,4,5,6,7,8,9]
    valueRandom: int = random.randint(rate[0, 9])
    if valueRandom > 0:
        value: int = 2
    else:
        value: int = 4
    i: int = random.randint(rate[0, 3])
    j: int = random.randint(rate[0, 3])
    issue[i][j].append(value)

'''
def fusion():
'''

def move(issue):    
    n = 0
    button : str = None
    while button != "Q" or button !="D" or button !="S":
        button: str = input("left: Q / right: D / down: S / up: Z \n").upper()
    for i in range(3):
        if button == "D":   
                issue[n][1] = issue[n][1] + issue[n+1][1]
        elif button == "Q":
            issue[n+1][1] = issue[n][1] + issue[n+1][1]
        elif button == "S":
            issue[n+10][1] = issue[n][1] + issue[n+10][1]
        elif button == "Z":
            issue[n][1] = issue[n][1] + issue[n+10][1]
move()

def game():
    os.system("cls")

game()