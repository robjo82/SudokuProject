import random, grids
grids.grid_creation()
grid_number = random.randint(1,10)
grid = grids.SudokuGrid.get_grid(grid_number)
print(grid)

print(grid)
