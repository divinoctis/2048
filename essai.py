grid: list[int] = [0, 0, 2, 2, 4, 5, 7]

print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])

print("Bonjour")
print("Bonjour")
print("Bonjour")
print("Bonjour")

def PrintGrid(grid):
    i = 0
    while i < 4:
        print(grid[i])
        i += 1

def HasNumber4(grid) -> bool:
    number4: bool = False
    i: int = 0
    while number4 == False:
        if grid[i] == 4:
            number4 == True
        else:
            i += 1







def move_left(grid):
    

    pass

move_left(grid)
    
print(grid)