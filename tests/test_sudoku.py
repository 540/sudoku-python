from hamcrest import assert_that, equal_to
from src.sudoku import Sudoku

def test_empty_board_is_invalid():
    sudoku = Sudoku([])

    assert_that(sudoku.validate(), equal_to("El input no cumple las reglas de Sudoku"))

def test_board_dimension_less_than_3_is_invalid():
    sudoku = Sudoku([[1,2],[3,4]])

    assert_that(sudoku.validate(), equal_to("El input no cumple las reglas de Sudoku"))
    
def test_every_board_row_must_contain_every_number_in_the_range():
    sudoku = Sudoku([[1,2,3],[1,3,2],[2,3,1]])

    assert_that(sudoku.validate(), equal_to("El input cumple las reglas de Sudoku"))

def test_board_row_must_not_contain_duplicates():
    sudoku = Sudoku([[1,2,2],[1,3,2],[3,1,2]])

    assert_that(sudoku.validate(), equal_to("El input no cumple las reglas de Sudoku"))