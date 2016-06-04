import numpy as np


def solve(sudoku):
    simple_cell = _get_simple_cell(sudoku)
    while simple_cell:
        print('\t\tSolving simple cell: {}'.format(simple_cell))
        _solve_simple_cells(sudoku, simple_cell)
        simple_cell = _get_simple_cell(sudoku)


def _solve_simple_cells(sudoku, simple_cell):
    i, j = simple_cell[0]
    value = simple_cell[1]
    if j == -1:
        row = sudoku.field[i]
        row[np.where(row == 0)[0][0]] = value
    elif i == -1:
        column = sudoku.field.transpose()[j]
        column[np.where(column == 0)[0][0]] = value
    else:
        square = sudoku.field[i:i + 3, j:j + 3]
        index = np.where(square == 0)
        sudoku.field[i + index[0][0], j + index[1][0]] = \
            value


def _get_simple_cell(sudoku):
    differences = sudoku.get_differences()
    print('\t\tGot differences: {}'.format(differences))
    simple_differences_indexes = [i for i in differences if len(differences[i]) == 1]
    if simple_differences_indexes:
        return simple_differences_indexes[0], differences[simple_differences_indexes[0]][0]
    return None
