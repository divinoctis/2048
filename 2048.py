import random


def board():
    issue = [
        [0,None], [1,None], [2,None], [3,None],
        [10, None], [11, None], [12, None], [13, None],
        [20,None], [21,None], [22, None], [23, None],
        [30, None], [31, None], [32, None], [33, None],
    ]

def randomShots():

    random: int = [0,1,2,3,4,5,6,7,8,9]
    value: int = random.randint([])
    if value > 0:
        value = 2
    else:
        value = 4

def move(issue):    
    n = 0
    button : str = None
    while button != "Q" or button !="D" or button !="S":
        button: str = input("left: Q / right: D / down: S \n").upper()
    for i in range(3):
        if button == "D":   
                issue[n+1][1] = issue[n][1]+ issue[n+1][1]
        elif button == "Q":
            issue[n-1][1] = issue[n][1]+ issue[n-1][1]
        elif button == "S":
            issue[n+10][1] = issue[n][1]+ issue[n+10][1]
move()