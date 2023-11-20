import numpy as np

class Validator(object):
    def validate(self, board):
        board = np.array(board)

        if (
            self._has_dimension_lower_than_4(board)
            or not self._is_square(board)
            or not self._validate_rows(board)
            or not self._validate_columns(board)
            or not self._validate_regions(board)
        ):
            return False

        return True

    def _has_dimension_lower_than_4(self, board):
        return len(board) < 4

    def _is_square(self, board):
        return len(board) == len(board[0])

    def _validate_rows(self, board):
        return all(self._validate_numbers(row) for row in board)

    def _validate_columns(self, board):
        return all(
            self._validate_numbers(column) for column in self._get_columns(board)
        )

    def _validate_regions(self, board):
        return all(
            self._validate_numbers(region) for region in self._get_regions(board)
        )

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
