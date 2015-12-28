import numpy as np


class Sudoku:
    "Class that represents sudoku table."
    _CORRECT_LINE = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        self.field = np.zeros((10, 10))

    def fill_field(self, field_param):
        self.field = np.array(field_param)

    def _check_lines(self):
        for i in range(9):
            if not sorted(self.field[i]) == self._CORRECT_LINE:
                print 'Lines check failed for the %d line.' % i
                return False
        return True

    def _check_columns(self):
        transpose_field = self.field.transpose()
        for i in range(9):
            if not sorted(transpose_field[i]) == self._CORRECT_LINE:
                print 'Columns check failed for the %d column.' % i
                return False
        return True

    def _check_square(self, i, j):
        square = []
        for k in range(i, i + 3):
            for l in range(j, j + 3):
                square.append(self.field[k][l])
        return sorted(square) == self._CORRECT_LINE

    def _check_squares(self):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self._check_square(i, j):
                    print 'Squares check failed for the ' \
                          '[%d, %d] square.' % (i, j)
                    return False
        return True

    def is_correct(self):
        return self._check_squares() and \
            self._check_lines() and \
            self._check_columns()

    def print_field(self):
        for i in range(9):
            if i % 3 == 0:
                print '-' * 37
            for j in range(9):
                if j % 3 == 0:
                    print '| ',
                print str(self.field[i][j]) + ' ',
            print '|'
        print '-' * 37
