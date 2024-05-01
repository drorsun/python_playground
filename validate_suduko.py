
def is_valid_sudoku(board: list[list[str]]) -> bool:
    # check basics
    if len(board) != 9:
        return f'only {len(board)} rows', False
    for row in board:
        if len(row) != 9:
            f'column has only {len(row)} items', False

    # rows and columns
    rows = board
    # columns = list(zip(*board)) #transposed
    columns = []
    for rownum in range(9):
       columns.append([row[rownum] for row in rows])

    squares = []
    for rownum in [0, 3, 6]:
        for sectnum in [0, 3, 6]:
            squares.append(rows[rownum][sectnum:sectnum+3] + rows[rownum+1][sectnum:sectnum+3] + rows[rownum+2][sectnum:sectnum+3])

    # validate all rows, columns and squares:
    for numlist in rows + columns + squares:
        counters = [0 for _ in range(9)]
        for numstr in numlist:
            if numstr.isdigit():
                num = int(numstr) - 1
                if counters[num] == 1:
                    return numstr, False
                counters[num] += 1
            elif numstr != '.':
                return numstr, False
    
    return None, True


if __name__ == '__main__':

    sudoku_grid = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    numstr, resp = is_valid_sudoku(sudoku_grid)
    if resp:
        print("Valid")
    else:
        print(f"Not Valid - {numstr}")

# You can solve the Sudoku by replacing the dots with valid numbers (1-9).
