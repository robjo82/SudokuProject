import random

grid = [
    [1,2,3,4,5,6,7,8,9],
    [2,3,4,5,6,7,8,9,1],
    [3,4,5,6,7,8,9,1,2],
    [4,5,6,7,8,9,1,2,3],
    [5,6,7,8,9,1,2,3,4],
    [6,7,8,9,1,2,3,4,5],
    [7,8,9,1,2,3,4,5,6],
    [8,9,1,2,3,4,5,6,7],
    [9,1,2,3,4,5,6,7,8]
]

def row_exchange(grid, row1, row2):
    temp = grid[row1]
    grid[row1] = grid[row2]
    grid[row2] = temp

def col_exchange(grid, col1, col2):
    for i in range(9):
        temp = grid[i][col1]
        grid[i][col1] = grid[i][col2]
        grid[i][col2] = temp

def print_grid(grid, ):
    for i in range(9):
        for j in range(9):
            print('\033[91m', grid[i][j], '\033[0m', end=" ")
        print()

for i in range (0, 100):
    row1 = random.randint(0,8)
    row2 = random.randint(0,8)
    col1 = random.randint(0,8)
    col2 = random.randint(0,8)
    row_exchange(grid, row1, row2)
    col_exchange(grid, col1, col2)
    print_grid(grid)
    print()


