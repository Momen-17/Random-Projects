import time
import random


class Sudoku:
    def __init__(self, grid):
        # Initialize sudoku grid
        self.grid = grid
    
    def print_grid(self):
        # Print every row of grid
        for row in self.grid:
            print(row)
    
    def solve(self, row=0, column=0):
        # Check if all rows are filled
        if row == 9:
            return True
        
        # Check if final column is reached
        elif column == 9:
            return self.solve(row + 1, 0)
        
        # Check cell isn't filled
        elif self.grid[row][column] != 0:
            return self.solve(row, column + 1)
        
        else:
            # Try a number 1-9
            for number in range(1, 10):
                # Check number is valid
                if self.is_valid(row, column, number):
                    # Append number to cell
                    self.grid[row][column] = number
                    # Check if number was correct
                    if self.solve(row, column + 1):
                        return True
                    # Remove number from cell
                    self.grid[row][column] = 0
            # If we checked all possible options and they all incorrect then grid has no solution
            return False
    
    def is_valid(self, row, column, number):
        # Check number in row
        if number in self.grid[row]:
            return False
        
        # Check number in column
        if number in (self.grid[i][column] for i in range(9)):
            return False
        
        # Check number in subgrid
        subgrid_start_row, subgrid_start_column = row // 3 * 3, column // 3 * 3
        # For every cell in row
        for i in range(subgrid_start_row, subgrid_start_row + 3):
            # For every cell in column
            for j in range(subgrid_start_column, subgrid_start_column + 3):
                # Check if cell equals number
                if self.grid[i][j] == number:
                    return False
        
        # If all check are passed
        return True


if __name__ == '__main__':
    # Store file names in a list
    file_names = ['Easy.seed', 'Medium.seed', 'Hard.seed', 'Extreme.seed', 'Unfair.seed']
    # Chose a random file and store it's difficulty
    file_name = random.choice(file_names)
    difficulty = file_name.split('.')[0]
    
    # Open file as read
    with open(file_name, 'r') as file:
        # Get a random line from file
        line = random.choice(file.readlines())[0:81]
    
    # Generate sudoku grid from the file
    grid = [list(map(lambda x: int(x) if x.isdigit() else 0, line[i:i+9])) for i in range(0, 81, 9)]
    
    # # Explaination: 
    # grid = []
    # for i in range(0, 81, 9):
    #     row = []
    #     for x in line[i:i+9]:
    #         if x.isdigit():
    #             row.append(int(x))
    #         else:
    #             row.append(0)
    #     grid.append(row)
    
    # Create sudoku object
    game = Sudoku(grid)
    
    # Print initial board
    print('Initial board: ')
    game.print_grid()
    print(f'Difficulty: {difficulty}')
    
    print()
    print('=' * 27)
    print()
    
    # Solve and print solved grid
    t1 = time.perf_counter()
    game.solve()
    t2 = time.perf_counter()
    game.print_grid()
    print()
    print(f'Solving time: {t2 - t1} seconds')
