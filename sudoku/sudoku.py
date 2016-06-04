import numpy as np


class Sudoku:
    _CORRECT_LINE = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        self.field = np.zeros((10, 10))

    def fill_field(self, field_param):
        self.field = np.array(field_param)

    def print_field(self):
        for i in range(9):
            if i % 3 == 0:
                print('-' * 37)
            for j in range(9):
                if j % 3 == 0:
                    print('| ', end=' ')
                print(str(self.field[i][j]) + ' ', end=' ')
            print('|')
        print('-' * 37)

    def is_correct(self):
        return not len(self.get_differences())

    def get_differences(self):
        differences = {}
        differences.update(self._check_lines())
        differences.update(self._check_columns())
        differences.update(self._check_squares())
        return differences

    def _check_lines(self):
        differences = {}
        for i in range(9):
            diff = np.setdiff1d(self._CORRECT_LINE, self.field[i])
            if diff.size:
                differences[(i, -1)] = diff
        return differences

    def _check_columns(self):
        transposed_field = self.field.transpose()
        differences = {}
        for i in range(9):
            diff = np.setdiff1d(self._CORRECT_LINE, transposed_field[i])
            if diff.size:
                differences[(-1, i)] = diff
        return differences

    def _check_square(self, i, j):
        square = []
        for k in range(i, i + 3):
            for l in range(j, j + 3):
                square.append(self.field[k][l])
        return np.setdiff1d(self._CORRECT_LINE, square)

    def _check_squares(self):
        differences = {}
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                diff = self._check_square(i, j)
                if diff.size:
                    differences[(i, j)] = diff
        return differences
