def options(sudoku_board: list, loc: tuple) -> list:
    possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row_values = []
    column_values = []
    possible_numbers = []

    # Extract the current cell value
    number = sudoku_board[loc[0]][loc[1]]

    if number == -1:
        # Get values from the same row
        for value in sudoku_board[loc[0]]:
            if value > -1:
                row_values.append(value)

        # Get values from the same column
        for i in range(len(sudoku_board)):
            column_value = sudoku_board[i][loc[1]]
            if column_value > -1:
                column_values.append(column_value)

        # Filter possible values not in row or column
        for value in possible_values:
            if value not in row_values and value not in column_values:
                possible_numbers.append(value)

        # Check the 3x3 subgrid
        invalid_numbers = []
        row_start = (loc[0] // 3) * 3
        col_start = (loc[1] // 3) * 3

        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                subgrid_value = sudoku_board[i][j]
                if subgrid_value != -1 and subgrid_value in possible_numbers:
                    invalid_numbers.append(subgrid_value)

        for i in invalid_numbers:
            if i in possible_numbers:
                possible_numbers.remove(i)

    return possible_numbers

def possible_digit(sudoku_board: list):
    possibilities = []

    for i in range(len(sudoku_board)):
        for j in range(len(sudoku_board)):
            if sudoku_board[i][j] != -1:
                possibilities.append([])
            else:
                possibilities.append(options(sudoku_board, (i, j)))

    return possibilities

def one_stage(sudoku_board: list, possibilities: list):
    min_possible_count = 8
    min_position = None
    all_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    success = True
    not_finished = False

    for i in range(81):
        row_index = i // 9
        col_index = i % 9

        if len(possibilities[i]) == 1:
            sudoku_board[row_index][col_index] = possibilities[i][0]
            possibilities[i] = []

        elif len(possibilities[i]) > 0:
            if len(possibilities[i]) < min_possible_count:
                min_possible_count = len(possibilities[i])
                min_position = (row_index, col_index)
                not_finished = True

    if not_finished:
        print(min_position, 'NOT_FINISH')
        return

    for row in range(9):
        if set(sudoku_board[row]) != set(all_digits):
            success = False

        column_values =  []
        for col in range(9):
            column_values.append(sudoku_board[col][row])

        if set(column_values) != set(all_digits):
            success = False

        values = []
        row_start = (row // 3) * 3
        col_start = (row % 3) * 3

        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                values.append(sudoku_board[i][j])

        if set(values) != set(all_digits):
            success = False

    if not success:
        print('FINISH_FAILURE')
    else:
        print('FINISH_SUCCESS')

board = [
    [5, 3, 2, 1, 7, 6, 8, 9, -1],
    [6, 4, 8, 2, -1, 9, 1, 5, 7],
    [-1, -1, 9, -1, -1, -1, -1, 6, -1],
    [-1, -1, -1, -1, 6, -1, -1, -1, 3],
    [-1, -1, -1, 8, -1, 3, -1, -1, 1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, 6, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 8, -1, -1, -1, 9]
]

board1 = [
    [5, 3, 1, 2, 7, 6, 4, 9, 8],
    [6, 2, 4, 3, 9, 8, 1, 5, 7],
    [7, 8, 9, 1, 4, 5, 3, 6, 2],
    [1, 4, 2, 7, 6, 9, 5, 8, 3],
    [9, 5, 6, 8, 2, 3, 7, 4, 1],
    [3, 7, 8, 4, 5, 1, 9, 2, 6],
    [2, 6, 5, 9, 3, 7, 8, 1, 4],
    [8, 9, 3, 6, 1, 4, 2, 7, 5],
    [4, 1, 7, 5, 8, 2, 6, 3, 9]
]

board2 = [
    [5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, -1, -1, -1, 1, -1, -1],
    [-1, -1, 9, -1, -1, -1, -1, 6, -1],
    [-1, -1, -1, -1, 6, -1, -1, -1, 3],
    [-1, -1, -1, 8, -1, 3, -1, -1, 1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, 6, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 8, -1, -1, -1, 9]
]

one_stage(board1, possible_digit(board1))
