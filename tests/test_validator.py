from hamcrest import assert_that, equal_to
from src.validator import Validator

def test_valid_board():
    validator = Validator()
    board = [[3,2,1,4],[1,4,3,2],[4,3,2,1],[2,1,4,3]]

    assert_that(validator.validate(board), equal_to(True))

def test_empty_board_is_invalid():
    validator = Validator()
    board = []

    assert_that(validator.validate(board), equal_to(False))

def test_board_dimension_less_than_4_is_invalid():
    validator = Validator()
    board = [[1,2],[3,4]]

    assert_that(validator.validate(board), equal_to(False))
    
def test_board_dimension_must_be_square():
    validator = Validator()
    board = [[1,2,3,4],[4,3,2,1]]

    assert_that(validator.validate(board), equal_to(False))
    
def test_board_must_not_contain_other_values_than_1_to_N_where_N_is_the_board_dimension():
    validator = Validator()
    board = [[0,2,3,4],[1,4,3,2],[4,2,3,1],[3,1,7,4]]

    assert_that(validator.validate(board), equal_to(False))

def test_board_row_must_not_contain_duplicates():
    validator = Validator()
    board = [[1,2,2,4],[1,4,3,2],[4,2,3,1],[3,1,2,4]]

    assert_that(validator.validate(board), equal_to(False))

def test_board_column_must_not_contain_duplicates():
    validator = Validator()
    board = [[1,2,3,4],[1,4,3,2],[4,2,3,1],[3,1,2,4]]

    assert_that(validator.validate(board), equal_to(False))

def test_board_region_must_not_contain_duplicates():
    validator = Validator()
    board = [[1,2,3,4],[4,1,2,3],[3,4,1,2],[2,3,4,1]]

    assert_that(validator.validate(board), equal_to(False))