import numpy as np

class Sudoku(object):
    def __init__(self, board):
        self.board = np.array(board)

    def validate(self):
        if (len(self.board) <= 3) or (len(self.board[0]) != len(self.board)):
            return "El input no cumple las reglas de Sudoku"

        if not self._validate_rows():
            return "El input no cumple las reglas de Sudoku"

        if not self._validate_columns():
            return "El input no cumple las reglas de Sudoku"

        if not self._validate_regions():
            return "El input no cumple las reglas de Sudoku"

        return "El input cumple las reglas de Sudoku"

    def _validate_rows(self):
        return all(self._validate_numbers(row) for row in self.board)

    def _validate_columns(self):
        return all(self._validate_numbers(column) for column in self._get_columns())

    def _validate_regions(self):
        return all(self._validate_numbers(region) for region in self._get_regions())

    def _get_columns(self):
        return zip(*self.board)

    def _get_regions(self):
        regions = []
        for i in range(0, len(self.board), 2):
            for j in range(0, len(self.board), 2):
                regions.append(self.board[i : i + 2, j : j + 2].flatten())
        return regions

    def _validate_numbers(self, number_set):
        values = list(range(1, len(number_set) + 1))
        return sorted(number_set) == values
