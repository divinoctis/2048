grid: list[int] = [0, 0, 2, 5, 2]

def PrintGrid(grid):
    i = 0
    while i < 4:
        print(grid[i])
        i += 1

def HasNumber4(grid) -> bool:
    number4: bool = False
    i: int = 0
    size: int = len(grid)
    while i < size:
        if grid[i] == 4:
            return True
        else:
            i += 1
    
HasNumber4(grid)