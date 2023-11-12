from hamcrest import assert_that, equal_to
from src.sudoku import Sudoku

def test_empty_board_is_invalid():
    sudoku = Sudoku([])

    assert_that(sudoku.validate(), equal_to("El input no cumple las reglas de Sudoku"))

def test_board_dimension_less_than_4_is_invalid():
    sudoku = Sudoku([[1,2],[3,4]])

    assert_that(sudoku.validate(), equal_to("El input no cumple las reglas de Sudoku"))
    
def test_board_dimension_must_be_square():
    sudoku = Sudoku([[1,2,3,4],[4,3,2,1]])

    assert_that(sudoku.validate(), equal_to("El input no cumple las reglas de Sudoku"))
    
def test_board_row_must_not_contain_other_values_than_1_to_N_where_N_is_the_board_dimension():
    sudoku = Sudoku([[0,2,3,4],[1,4,3,2],[4,2,3,1],[3,1,7,4]])

    assert_that(sudoku.validate(), equal_to("El input no cumple las reglas de Sudoku"))

def test_board_row_must_not_contain_duplicates():
    sudoku = Sudoku([[1,2,2,4],[1,4,3,2],[4,2,3,1],[3,1,2,4]])

    assert_that(sudoku.validate(), equal_to("El input no cumple las reglas de Sudoku"))

def test_board_column_must_not_contain_other_values_than_1_to_N_where_N_is_the_board_dimension():
    sudoku = Sudoku([[0,2,3,4],[1,4,3,2],[4,2,3,1],[3,1,7,4]])

    assert_that(sudoku.validate(), equal_to("El input no cumple las reglas de Sudoku"))
