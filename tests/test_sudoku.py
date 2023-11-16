from hamcrest import assert_that, equal_to
from src.csvReader import CsvReader
from src.validator import Validator
from src.sudoku import Sudoku

def test_valid_sudoku():
    reader = CsvReader()
    validator = Validator()
    sudoku = Sudoku(reader, validator)

    assert_that(sudoku.game('correct_board_4x4.csv'), equal_to('El input cumple las reglas de Sudoku'))


def test_invalid_sudoku():
    reader = CsvReader()
    validator = Validator()
    sudoku = Sudoku(reader, validator)

    assert_that(sudoku.game('incorrect_board_4x4.csv'), equal_to('El input no cumple las reglas de Sudoku'))
