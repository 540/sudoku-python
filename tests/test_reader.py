from hamcrest import assert_that, equal_to
from src.Reader.csvReader import CsvReader

def test_read_csv():
    reader = CsvReader()
    expectedResult = [[3, 2, 1, 4], [1, 4, 3, 2], [4, 3, 2, 1], [2, 1, 4, 3]]
    
    assert_that(reader.read('correct_board_4x4'), equal_to(expectedResult))
