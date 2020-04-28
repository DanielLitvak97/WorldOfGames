from InputNumbersOnly import only_numbers
from random import randint
from time import sleep
from Utils import Screen_cleaner


def generate_sequence(difficulty):
    random_list = []
    for i in range(difficulty):
        random_list.append(randint(1, 101))
    print(random_list)
    sleep(0.7)
    Screen_cleaner()
    return random_list


def get_list_from_user(difficulty):
    user_list = []
    for i in range(difficulty):
        user_list.append(only_numbers(["Enter here the the number you saw in index number " + str(i + 1) + ": "]))
    return user_list


def is_list_equal(user_list, random_list):
    return user_list == random_list


def play(difficulty):
    if is_list_equal(generate_sequence(difficulty), get_list_from_user(difficulty)):
        print(True)
        return True
    else:
        print(False)


