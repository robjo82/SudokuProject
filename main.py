#SudokuProjects main file.
import random

def print_grid(grid, editable_cells):
    for row in grid:
        for col in row:
            if (row, col) in editable_cells:
                print('\033[92m', grid[row][col], '\033[0m', end=" ")
            else:
                print('\033[91m', grid[row][col], '\033[0m', end=" ")

def grid_generation(grid, level):
    returned_grid = grid.copy()
    editable_cells = []
    for i in range(2*level + 20):
        row = random.randint(0,8)
        col = random.randint(0,8)
        returned_grid[row][col] = 0
        editable_cells.append((row, col))
    return (returned_grid, editable_cells)

def test_value(grid, row, col, value):
    # Check row
    for i in range(9):
        if grid[row][i] == value:
            return False
    # Check column
    for i in range(9):
        if grid[i][col] == value:
            return False
    # Check box
    for i in range(3):
        for j in range(3):
            if grid[row-row%3+i][col-col%3+j] == value:
                return False
    return True

def test_grid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False
    return True

def game_loop():
    grid = 
    print_grid(grid, editable_cells)
    while not test_grid(grid):
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        value = int(input("Enter value: "))
        if test_value(grid, row, col, value):
            grid[row][col] = value
        else:
            print("Invalid value")
    print("You win!")





print_grid(grid_generation(grid_init(9)))