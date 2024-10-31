import words_fetcher
import random


def congratulate_user():
    print("=============================")
    print("= Congratulations! You won! =")
    print("=============================")


def is_game_over():
    return guessed == WORDS_TO_WIN or errors == ERRORS_TO_LOSE

def input_validation(guess, words_duplicates):
    while True:
        if guess in words_duplicates:
            print("You've already entered this word. Try a new one")
            guess = input("Your next take: ")
        else:
            return False



guessed = 0
errors = 0

WORDS_TO_WIN = 5
ERRORS_TO_LOSE = 3

words_duplicates = []

words = words_fetcher.fetch_words(min_letters=9, max_letters=9)
full_list = words_fetcher.fetch_words(min_letters=3, max_letters=9)
word = words[random.randrange(0, len(words))]

print(f"Can you make up {WORDS_TO_WIN} words from letters in word provided by me?")
print(f"Your word is '{word}'")


while not is_game_over():
    guess = input("Your next take: ")
    if guess in full_list:
        guessed += 1
        input_validation(guess, words_duplicates)
        words_duplicates.append(guess)
        if guessed == WORDS_TO_WIN:
            congratulate_user()
            exit()
        print(f"That's right! {WORDS_TO_WIN - guessed} to go")
    else:
        errors += 1
        print(f"Oops :( No such word, you have {ERRORS_TO_LOSE - errors} lives more")
    if ERRORS_TO_LOSE==errors:
        print(':(')
        print('You lose')
        print(':(')
        break