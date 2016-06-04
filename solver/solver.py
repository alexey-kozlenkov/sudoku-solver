import itertools


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
        index = row.index(0)
        sudoku.field[i][index] = value
    elif i == -1:
        column = sudoku.get_transposed_field()[j]
        index = column.index(0)
        sudoku.field[index][j] = value
    else:
        square = [line[j:j + 3] for line in sudoku.field[i:i + 3]]
        united_square = list(itertools.chain.from_iterable(square))
        index = united_square.index(0)
        sudoku.field[i + int(index / 3)][j + index % 3] = value


def _get_simple_cell(sudoku):
    differences = sudoku.get_differences()
    print('\t\tGot differences: {}'.format(differences))
    simple_differences_indexes = [i for i in differences if len(differences[i]) == 1]
    if simple_differences_indexes:
        return simple_differences_indexes[0], differences[simple_differences_indexes[0]].pop()
    return None
