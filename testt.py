import random
import os

def board():
    grid = []
    for i in range(0, 4):
        grid.append([0] * 4)
    return grid

# fonction à modifier pour rendre robuste le jeu
def ask_input(sMessage: str, char_auto: list[str]) -> str:
    while True:
        Input: str = input(sMessage).lower()
        if Input in char_auto:
            return str(Input)
        print("Ce n'est pas une réponse valable.")

def randomShots(grid):
    for i in range(2):
        valueRandom = random.randint(0, 9)
        if valueRandom > 0:
            value = 2
        else:
            value = 4
        while True:
            i = random.randint(0, 3)
            j = random.randint(0, 3)
            if grid[i][j] == 0:
                grid[i][j] = value
                break

def displayBoard(grid):
    for row in grid:
        print(row)

def move(grid, direction):
    if direction == "Q":
        for i in range(4):
            grid[i] = merge(grid[i])
    elif direction == "D":
        for i in range(4):
            grid[i] = merge(grid[i][::-1])[::-1]
    elif direction == "Z":
        for j in range(4):
            column = [grid[i][j] for i in range(4)]
            merged_column = merge(column)
            for i in range(4):
                grid[i][j] = merged_column[i]
    elif direction == "S":
        for j in range(4):
            column = [grid[i][j] for i in range(4)][::-1]
            merged_column = merge(column)[::-1]
            for i in range(4):
                grid[i][j] = merged_column[i]

def merge(line):
    merged_line = [0] * 4
    index = 0
    for i in range(4):
        if line[i] != 0:
            if merged_line[index] == 0:
                merged_line[index] = line[i]
            elif merged_line[index] == line[i]:
                merged_line[index] *= 2
                index += 1
            else:
                index += 1
                merged_line[index] = line[i]
    return merged_line

if __name__ == "__main__":
    grid = board()
    randomShots(grid)
    displayBoard(grid)

def game():
    randomShots(grid)
    while True:
        direction = input("left: Q / right: D / down: S / up: Z / quit: X \n").upper()
        if direction == "X":
            break

        move(grid, direction)
        randomShots(grid)
        displayBoard(grid)
        
game()