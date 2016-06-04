from copy import deepcopy


class Sudoku:
    correct_line = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __init__(self):
        self.field = [[0] * 10 for _ in range(9)]

    def fill_field(self, field_param):
        self.field = deepcopy(field_param)

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
            diff = self.correct_line - set(self.field[i])
            if diff:
                differences[(i, -1)] = diff
        return differences

    def _check_columns(self):
        transposed_field = self.get_transposed_field()
        differences = {}
        for i in range(9):
            diff = self.correct_line - set(transposed_field[i])
            if diff:
                differences[(-1, i)] = diff
        return differences

    def _check_square(self, i, j):
        square = []
        for k in range(i, i + 3):
            for l in range(j, j + 3):
                square.append(self.field[k][l])
        return self.correct_line - set(square)

    def _check_squares(self):
        differences = {}
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                diff = self._check_square(i, j)
                if diff:
                    differences[(i, j)] = diff
        return differences

    def get_transposed_field(self):
        return list(map(list, zip(*self.field)))
