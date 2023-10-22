import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    difficulty = input("Choose a level of difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess_num, rand_num, attempts):
    if guess_num > rand_num:
        print("Too high")
        return attempts - 1
    elif guess_num < rand_num:
        print("Too low")
        return attempts - 1
    else:
        print(f"You got it! The answer is {rand_num}")


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = set_difficulty()
    answer = random.randint(1, 100)
    guess = 0
    while guess != answer:
        print(f"You've {attempts} attempts to guess the number.")

        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)

        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")

game()
