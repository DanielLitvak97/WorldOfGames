from InputNumbersOnly import only_numbers
from MemoryGame import play as play_memory_game
from GuessGame import play as play_guess_game
from CurrencyRouletteGame import play as play_currency_roulette_game
from Scores import add_score


def welcome():
    print("Hello " + input("Please enter your name here: ") + " and welcome to the World of Games (WoG)." +
          "\n" + "Here you can find many cool games to play." + "\n")


def load_game():
    print("""Please choose a game to play:
       1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
       2. Guess Game - guess a number and see if you chose like the computer
       3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")

    game_number = only_numbers(["Enter here the game number: ", 1, 3])
    game_difficulty = only_numbers(["Please choose game difficulty from 1 to 5: ", 1, 5])

    if game_number == 1:
        if play_memory_game(game_difficulty):
            add_score(game_difficulty)
    if game_number == 2:
        if play_guess_game(game_difficulty):
            add_score(game_difficulty)
    if game_number == 3:
        if play_currency_roulette_game(game_difficulty):
            add_score(game_difficulty)


