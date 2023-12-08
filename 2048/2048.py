import random


startGrid : list[list[int]] = [
    
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],

]
grid = startGrid
checkGrid = startGrid


def randomShots(grid):
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


def PrintGrid(grid):
    for row in grid:
        print(row)


def move(grid, direction):
    i: int = 0
    while i < 4:
        if direction == "Q":
            n : int = 0
            while n < len(grid[i]):
                k: int = 1
                while n + k < len(grid[i]) and grid[i][n + k] == 0:
                    k += 1
                if n + k < len(grid[i]):
                    if grid[i][n] == grid[i][n + k] and grid[i][n + k] > 0:
                        grid[i][n] *= 2
                        grid[i][n + k] = 0
                    elif grid[i][n] == 0 and grid[i][n + k] > 0:
                        if n+k < len(grid[i]) -1 and grid[i][n + k] != grid[i][n + k + 1]:
                            grid[i][n] = grid[i][n + k]
                            grid[i][n + k] = 0
                        elif n+k == len(grid[i]) -1:
                            grid[i][n] = grid[i][n + k]
                            grid[i][n + k] = 0
                        if n-1 > -1 and grid[i][n] == grid[i][n-1]:
                            grid[i][n-1] *= 2
                            grid[i][n] = 0
                n += 1

        elif direction == "D":
            n: int = len(grid[i]) - 1
            while n >= 0:
                k: int = 1
                while n - k >= 0 and grid[i][n - k] == 0:
                    k += 1
                if n - k >= 0:
                    if grid[i][n] == grid[i][n - k] and grid[i][n - k] > 0:
                        grid[i][n] *= 2
                        grid[i][n - k] = 0
                    elif grid[i][n] == 0 and grid[i][n - k] > 0:
                        if n - k > 0 and grid[i][n - k] != grid[i][n - k - 1]:
                            grid[i][n] = grid[i][n - k]
                            grid[i][n - k] = 0
                        elif n - k == 0:
                            grid[i][n] = grid[i][n - k]
                            grid[i][n - k] = 0
                        if n + 1 < len(grid) and grid[i][n] == grid[i][n + 1]:
                            grid[i][n + 1] *= 2
                            grid[i][n] = 0
                n -= 1
        
        elif direction == "Z":
            n : int = 0
            while n < len(grid):
                k: int = 1
                while n + k < len(grid) and grid[n + k][i] == 0:
                    k += 1
                if n + k < len(grid):
                    if grid[n][i] == grid[n + k][i] and grid[n + k][i] > 0:
                        grid[n][i] *= 2
                        grid[n + k][i] = 0
                    elif grid[n][i] == 0 and grid[n + k][i] > 0:
                        if n+k < len(grid) -1 and grid[n + k][i] != grid[n + k + 1][i]:
                            grid[n][i] = grid[n + k][i]
                            grid[n + k][i] = 0
                        elif n+k == len(grid) -1:
                            grid[n][i] = grid[n + k][i]
                            grid[n + k][i] = 0
                        if n-1 > -1 and grid[n][i] == grid[n - 1][i]:
                            grid[n - 1][i] *= 2
                            grid[n][i] = 0
                n += 1

        elif direction == "S":
            n: int = len(grid) - 1
            while n >= 0:
                k: int = 1
                while n - k >= 0 and grid[n - k][i] == 0:
                    k += 1
                if n - k >= 0:
                    if grid[n][i] == grid[n - k][i] and grid[n - k][i] > 0:
                        grid[n][i] *= 2
                        grid[n - k][i] = 0
                    elif grid[n][i] == 0 and grid[n - k][i] > 0:
                        if n - k > 0 and grid[n - k][i] != grid[n - k - 1][i]:
                            grid[n][i] = grid[n - k][i]
                            grid[n - k][i] = 0
                        elif n - k == 0:
                            grid[n][i] = grid[n - k][i]
                            grid[n - k][i] = 0
                        if n + 1 < len(grid) and grid[n][i] == grid[n + 1][i]:
                            grid[n + 1][i] *= 2
                            grid[n][i] = 0
                n -= 1
        elif direction == "X":
            grid[0][0] = 2048

        i+=1


def checkLoose(grid,direction):

    for row in grid:
        for value in row:
            if value == 0:
                return False
    
    checkGrid = grid
    direction == "Z"
    move(checkGrid, direction)
    for row in checkGrid:
        for value in row:
            if checkGrid[row][value] != grid[row][value]:
                return False 

    checkGrid = grid
    direction == "S"
    move(checkGrid, direction)
    for row in checkGrid:
        for value in row:
            if checkGrid[row][value] != grid[row][value]:
                return False 

    checkGrid = grid
    direction == "Q"
    move(checkGrid, direction)
    for row in checkGrid:
        for value in row:
            if checkGrid[row][value] != grid[row][value]:
                return False 

    checkGrid = grid
    direction == "D"
    move(checkGrid, direction)
    for row in checkGrid:
        for value in row:
            if checkGrid[row][value] != grid[row][value]:
                return False 
    return True


def checkWin(grid):
    for row in grid:
        for value in row:
            if value == 2048:
                return True
    return False


def game():
    restart : str = "oui"
    while restart == "oui":
        grid = startGrid
        randomShots(grid)
        win : bool = False
        loose : bool = False
        while win == False or loose == False:
            randomShots(grid)
            PrintGrid(grid)
            direction : str = input("Z, Q, S or D : ").upper()
            move(grid,direction)
            win = checkWin(grid)
            loose = checkLoose(grid,direction)
        PrintGrid(grid)
        if win == True:
            print('\nVous avez gagné!\n')
        else:
            print('\nVous avez perdu...\n')
        restart : str = input("taper 'oui' pour rejouer ou autre pour arrêter: ")

game()
