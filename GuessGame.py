from InputNumbersOnly import only_numbers
from random import randint


def generate_number(difficulty):
    secret_number = randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    return only_numbers(["Please guess a number from 1 to " + str(difficulty) + ": ", 1, difficulty])


def compare_results(secret_number, guess):
    return secret_number == guess


def play(difficulty):
    if compare_results(generate_number(difficulty), get_guess_from_user(difficulty)):
        print(True)
    print(False)







