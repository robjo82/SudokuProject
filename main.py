#SudokuProjects main file.
import random
import grids

def print_grid(grid, editable_cells):
    for i in range(9):
        for j in range(9):
            if (i, j) in editable_cells :
                print('\033[92m', grid[i][j], '\033[0m', end=" ")
            else:
                print('\033[91m', grid[i][j], '\033[0m', end=" ")
        print()

def grid_generation(grid, level):
    returned_grid = grid.copy()
    editable_cells = []
    for i in range(2*level + 20):
        while True :
            row = random.randint(0,8)
            col = random.randint(0,8)
            if (row, col) not in editable_cells:
                returned_grid[row][col] = 0
                editable_cells.append((row, col))
                break
    return (returned_grid, editable_cells)

def test_value(grid, row, col, value):
    # Check row
    for i in range(9):
        if grid[row][i] == value:
            print("Value already in row")
            return False
    # Check column
    for i in range(9):
        if grid[i][col] == value:
            print("Value already in column")
            return False
    # Check box
    for i in range(3):
        for j in range(3):
            if grid[row-row%3+i][col-col%3+j] == value:
                print("Value already in box")
                return False
    return True

def test_grid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False
    return True

def game_loop():
    grid_number = random.randint(1,10)
    grids.grid_creation()
    starting_grid = grids.SudokuGrid.get_grid(grid_number)

    level = int(input("Enter difficulty level (1-10): "))
    playing_grid = grid_generation(starting_grid, level)
    grid = playing_grid[0]
    editable_cells = playing_grid[1]

    
    print_grid(grid, editable_cells)
    while not test_grid(grid):
        row = int(input("Enter row between 1 and 9 : ")) - 1
        col = int(input("Enter column between 1 and 9 : ")) - 1
        value = int(input("Enter value between 1 and 9 : "))


        if (row, col) in editable_cells :
            if test_value(grid, row, col, value) :
                grid[row][col] = value
            else:
                print("Invalid value")
        else:
            print("Cell is not editable")
        print_grid(grid, editable_cells)
    print("You win!")

game_loop()