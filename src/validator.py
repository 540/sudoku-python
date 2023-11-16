import numpy as np

class Validator(object):
    
    def validate(self, board):
        board = np.array(board)

        if (len(board) <= 3) or (len(board[0]) != len(board)):
            return "El input no cumple las reglas de Sudoku"

        if not self._validate_rows(board):
            return "El input no cumple las reglas de Sudoku"

        if not self._validate_columns(board):
            return "El input no cumple las reglas de Sudoku"

        if not self._validate_regions(board):
            return "El input no cumple las reglas de Sudoku"

        return "El input cumple las reglas de Sudoku"

    def _validate_rows(self, board):
        return all(self._validate_numbers(row) for row in board)

    def _validate_columns(self, board):
        return all(self._validate_numbers(column) for column in self._get_columns(board))

    def _validate_regions(self, board):
        return all(self._validate_numbers(region) for region in self._get_regions(board))

    def _get_columns(self, board):
        return zip(*board)

    def _get_regions(self, board):
        regions = []
        for i in range(0, len(board), 2):
            for j in range(0, len(board), 2):
                regions.append(board[i : i + 2, j : j + 2].flatten())
        return regions

    def _validate_numbers(self, number_set):
        values = list(range(1, len(number_set) + 1))
        return sorted(number_set) == values
