import pyautogui as pg
import numpy as np
import time

#grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
#        [5, 2, 0, 0, 0, 0, 0, 0, 0],
#        [0, 8, 7, 0, 0, 0, 0, 3, 1],
#        [0, 0, 3, 0, 1, 0, 0, 8, 0],
#        [9, 0, 0, 8, 6, 3, 0, 0, 5],
#        [0, 5, 0, 0, 9, 0, 6, 0, 0],
#        [1, 3, 0, 0, 0, 0, 2, 5, 0],
#        [0, 0, 0, 0, 0, 0, 0, 7, 4],
#        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def insert_grid():
    grid = []
    while True:
        row = list(input("Insert Row: "))
        ints = []

        for n in row:
            ints.append(int(n))
        grid.append(ints)

        if len(grid) == 9:
            break
        print("Row " + str(len(grid)) + ' completed')
    return grid


def put(matrix):

    counter = []
    str_final = list(np.array(matrix).astype(str).flatten())

    for number in str_final:
        pg.press(number)
        pg.hotkey('right')

        counter.append(number)
        if len(counter) % 9 == 0:
            pg.hotkey('down')

            # go left
            for i in range(9):
                pg.hotkey('left')


def board_print(board):
    """
    Prints 9x9 numpy array input board in an easier to read format.
    """

    board = np.array(board)

    # Some basic checks
    assert board.shape == (9, 9)
    assert type(board) == np.ndarray

    # Convert array elements to strings
    board_str = board.astype(str)

    # Our row separator
    row_sep = '-' * 25

    # Loop through 9 rows
    for i in range(9):

        # At each multiple of 3, print row separator
        if i % 3 == 0:
            print(row_sep)

        # Get row data
        row = board_str[i]

        # Format row of data with pipe separators at each end, and between each sub grid
        print('| ' + ' '.join(row[0:3]) + ' | ' + ' '.join(row[3:6]) + ' | ' + ' '.join(row[6:]) + ' |')

    # Print final row separator at bottom after loops finish
    print(row_sep)


def is_valid_move(grid, row, col, number):
    # is there something in the same block, row, or col

    # check for row
    for column in range(9):
        if grid[row][column] == number:
            return False

    # check for column
    for x in range(9):
        if grid[x][col] == number:
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

    if row == 8 and col == 9:
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


grid = insert_grid()
time.sleep(2)

if solve(grid, 0, 0):
    put(grid)
    print("This is the final solution:\n\n\n")
    board_print(grid)

else:
    print("there is no possible solution")
