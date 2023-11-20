class Sudoku():
    def __init__(self, reader, validator, notifier):
        self.reader = reader
        self.validator = validator
        self.notifier = notifier
    
    def game(self, filename):
        board = self.reader.read(filename)
        isValid = self.validator.validate(board)

        if not isValid:
            return self.notifier.notify('El input no cumple las reglas de Sudoku')

        return self.notifier.notify('El input cumple las reglas de Sudoku')        


