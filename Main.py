import sys
from src.Notifier.stdoutNotifier import StdoutNotifier
from src.Reader.csvReader import CsvReader
from src.validator import Validator
from src.sudoku import Sudoku

if len(sys.argv) > 1:
    reader = CsvReader()
    validator = Validator()
    notifier = StdoutNotifier()
    sudoku = Sudoku(reader, validator, notifier)

    filename = sys.argv[1]

    sudoku.game(filename)
