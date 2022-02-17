from dataclasses import dataclass
from termcolor import colored
from source.word_list import random_word_list
import random


@dataclass
class Answer:
    raw: str
    chars: list
    length: int

@dataclass
class Guess:
    raw: str
    chars: list
    length: int

@dataclass
class GridChar:
    char: str = '0'
    color: str = 'grey'

class GridRow:
    row: list[GridChar]
    row_idx: str

@dataclass
class Grid:
    row_count: int
    col_count: int
    grid_list: list[GridRow]
    status: bool = False

    def show(self):
        for row in self.grid_list:
            for char in row:
                print(colored(char.char, char.color), end=" ")
            print("\n")
