from pprint import pprint

grid = [[2, 0, 9, 0, 0, 0, 6, 0, 0],
        [0, 4, 0, 8, 7, 0, 0, 1, 2],
        [8, 0, 0, 0, 1, 9, 0, 4, 0],
        [0, 3, 0, 7, 0, 0, 8, 0, 1],
        [0, 6, 5, 0, 0, 8, 0, 3, 0],
        [1, 0, 0, 0, 3, 0, 0, 0, 7],
        [0, 0, 0, 6, 5, 0, 7, 0, 9],
        [6, 0, 4, 0, 0, 0, 0, 2, 0],
        [0, 8, 0, 3, 0, 1, 4, 5, 0]]


def display(board):
    """Prints the sudoku board"""
    ROWS = COLS = 9
    GRID_ROWS = GRID_COLS = 3

    print()

    for row in range(ROWS):
        s = ''

        for col in range(COLS):
            s += str(board[row][col]) + ' '

            if not (col + 1) % GRID_COLS:
                s += '| '

        s = s[:-1]  # Removes trailing space

        print(s)

        if not (row + 1) % GRID_ROWS:
            print('-' * len(s))


def is_valid_move(grid, row, col, number):
    # is there something in the same block, row, or col

    # check for row
    for column in range(9):
        if grid[row][column] == number:
            return False

    # check for column
    for x in range(9):
        if grid[row][x] == number:
            return False

    # check for block
    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False

    return True


def solve(grid, row, col):

    # solve from this particular position
    # stop backtracking, return true
    if col == 9 and row == 8:
        return True

    if col == 9:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    for num in range(1, 10):

        if is_valid_move(grid, row, col, num):

            grid[row][col] = num

            if solve(grid, row, col + 1):
                return True

        grid[row][col] = 0

    return False


if solve(grid, 0, 0):
    display(grid)
else:
    print("It seems like this Sudoku doesn't have a solution")
