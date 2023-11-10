import numpy as np

class Sudoku(object):    
    def __init__(self, board):
        self.board = board

    def validate(self):
        if (len(self.board) < 3) or (len(self.board[0]) != len(self.board)):
            return "El input no cumple las reglas de Sudoku"
        
        if not self._validate_rows():
            return "El input no cumple las reglas de Sudoku"
    
        return "El input cumple las reglas de Sudoku"
    
    def _validate_rows(self):
        return all(self._validate_row(row) for row in self.board)
    
    def _validate_row(self, row):
        values = list(range(1, len(row) + 1))
        return sorted(row) == values

    