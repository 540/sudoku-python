import csv
from src.Reader.Reader import Reader

class CsvReader(Reader):
    def read(self, filename) -> list:
        matrix = []
        with open(f"./src/boards/{filename}.csv", "r", encoding="utf-8") as file:
            matrix = [
                [int(element) for element in row if element.strip()]
                for row in csv.reader(file, delimiter=",")
            ]

        return matrix
