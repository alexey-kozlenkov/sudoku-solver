#!/usr/bin/env python
import numpy as np


class Sudoku:
    "Class that represents sudoku table."
    _CORRECT_LINE = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        self.field = np.zeros((10, 10))

    def fill_field(self, field_param):
        self.field = np.array(field_param)

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

    def _check_lines(self):
        for i in range(9):
            if np.setdiff1d(self.field[i], self._CORRECT_LINE).size:
                return (i, -1)
        return None

    def _check_columns(self):
        transposed_field = self.field.transpose()
        for i in range(9):
            if np.setdiff1d(transposed_field[i], self._CORRECT_LINE).size:
                return (-1, i)
        return None

    def _check_square(self, i, j):
        square = []
        for k in range(i, i + 3):
            for l in range(j, j + 3):
                square.append(self.field[k][l])
        return np.setdiff1d(square, self._CORRECT_LINE).size

    def _check_squares(self):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if self._check_square(i, j):
                    return (i, j)
        return None

    def is_correct(self):
        return self._check_squares() or \
            self._check_lines() or \
            self._check_columns() or \
            True
