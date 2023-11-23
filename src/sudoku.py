from src.Notifier import Notifier
from src.Reader import Reader
from src.validator import Validator


class Sudoku:
    def __init__(self, reader: Reader, validator: Validator, notifier: Notifier):
        self.reader = reader
        self.validator = validator
        self.notifier = notifier

    def game(self, filename: str):
        board = self.reader.read(filename)
        isValid = self.validator.validate(board)

        if not isValid:
            self.notifier.notify("El input no cumple las reglas de Sudoku")
        else:
            self.notifier.notify("El input cumple las reglas de Sudoku")
