from main import get_random_word, get_answer, get_grid, get_guess, compare_answer, main
from source.dataclass import Guess, Answer, Grid, GridChar

import pytest

def test_get_random_word():
    random_word = get_random_word()
    assert type(random_word) == str

def test_get_answer():
    answer = get_answer()
    assert type(answer.raw) == str
    assert len(answer.chars) == answer.length
    assert answer.status == False


def test_get_grid():
    grid = get_grid(row_count=5, col_count=5)
    assert len(grid.grid_list[0]) == grid.col_count
    assert len(grid.grid_list) == grid.row_count



@pytest.mark.parametrize("answer_length,guess_raw", [(5, "plane")])
def test_get_guess(answer_length, guess_raw):
    guess = get_guess(answer_length, guess_raw)
    assert guess.length == 5
    assert guess.status == False


def test_compare_answer():
    return

def test_main():
    return