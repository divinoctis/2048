grid: list[int] = [0, 0, 2, 2]


def PrintGrid(grid):
    i = 0
    while i < 4:
        print(grid[i])
        i += 1

def move_left(grid):
    direction : str = input("Q").upper()
    n : int = 0
    k: int = 1
    if direction == "Q":
        while n < len(grid):
            while n+k < len(grid) and grid[n+k] == 0:
                k += 1

            if n+k < len(grid):
                grid[n] = grid[n + k]
                grid[n + k] = 0

            k = 1
            n += 1
            

print(grid)
move_left(grid)
print(grid)