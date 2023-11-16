class Sudoku():
    def __init__(self, reader, validator):
        self.reader = reader
        self.validator = validator
    
    def game(self, filename):
        board = self.reader.read(filename)
        return self.validator.validate(board)
    