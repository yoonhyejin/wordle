import termcolor

from source.word_list import random_word_list
from source.dataclass import Guess, Answer, Grid, GridChar
from source.word_list import random_word_list

import random

def get_random_word(random_word_list=random_word_list):
    return random.choice(random_word_list)

def get_answer() -> Answer:
    random_word = get_random_word()
    random_word_chars = list(random_word.strip(" "))
    answer = Answer(raw=random_word,
                    chars=random_word_chars,
                    length=len(random_word))
    return answer

def get_grid(row_count, col_count) -> Grid:
    grid_list = [[GridChar()]* row_count for _ in range(col_count)]
    grid = Grid(row_count=row_count,
                col_count=col_count,
                grid_list=grid_list)
    return grid


def get_guess(answer_length, guess_raw=None):
    if not guess_raw:
       guess_raw = input("Your Guess: ...")
    if len(guess_raw) != answer_length:
        print(f"Length should be {answer_length}.")
    guess_chars = list(guess_raw.strip(" "))
    # 나중에, 맞는 단어인지 확인
    # elif guess not in rigthtful_word_list:
    #     print("Please type right word.")
    guess = Guess(raw=guess_raw,
                  chars=guess_chars,
                  length=len(guess_raw))
    return guess

def compare_answer(grid, idx, guess, answer):
    row = grid.grid_list[idx]
    for _idx in range(guess.length):
        if guess.chars[_idx] == answer.chars[_idx]:
            row[_idx] = GridChar(char=guess.chars[_idx], color='green')
        elif guess.chars[_idx] in answer.chars:
            row[_idx] = GridChar(char=guess.chars[_idx], color='yellow')
        else:
            row[_idx] = GridChar(char=guess.chars[_idx], color='red')
    grid.grid_list[idx] = row
    return grid


def main():
    answer = get_answer()
    grid = get_grid(row_count=answer.length, col_count=5)
    grid.show()
    print(answer.raw)
    for idx in range(grid.row_count):
        guess = get_guess(answer_length=answer.length)
        grid = compare_answer(grid, idx, guess, answer)
        grid.show()
        if answer.raw == guess.raw:
            grid.status == True
            break
        else:
            print(f"You wrong!")

    grid.show()
    print(f"You won! Answer is {answer.raw}!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()