grid: list[int] = [0, 0, 2, 2]


def PrintGrid(grid):
    i = 0
    while i < 4:
        print(grid[i])
        i += 1

def moveHorizontal(grid):
    direction : str = input("Q or D : ").upper()
    
    if direction == "Q":
        n : int = 0
        k: int = 1
        while n < len(grid):
            while n+k < len(grid) and grid[n+k] == 0:
                k += 1
            if n+k < len(grid):
                grid[n] = grid[n + k]
                grid[n + k] = 0
            k = 1
            n += 1
    elif direction == "D":
        n : int = len(grid)
        k: int = -1
        while n > 0:
            while n+k > 0 and grid[n+k] == 0:
                k -= 1
            if n+k > 0:
                grid[n] = grid[n + k]
                grid[n + k] = 0
            k = -1
            n -= 1
        
           
print(grid)
for i in range(2):
    moveHorizontal(grid)
    print(grid)