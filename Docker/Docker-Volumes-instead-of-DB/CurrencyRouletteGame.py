from InputNumbersOnly import only_numbers
from currency_converter import CurrencyConverter
from random import randint


def get_money_interval(difficulty, money):
    c = CurrencyConverter()
    currency = c.convert(money, 'USD', 'ILS')
    return [currency - (5 - difficulty), currency + (5 - difficulty)]


def get_guess_from_user(money):
    return float(only_numbers(["What do you think approximately is the currency of " + str(money) + " from USD to ILS? "]))


def play(difficulty):
    money = randint(1, 100)
    money_interval = get_money_interval(difficulty, money)
    if money_interval[0] <= get_guess_from_user(money) <= money_interval[1]:
        print(True)
        return True
    else:
        print(False)



