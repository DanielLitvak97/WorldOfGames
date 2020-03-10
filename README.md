# WorldOfGames

----Python----
I created several games using python scripts.

The games:
CurrencyRouletteGame.py
GuessGame.py
MemoryGame.py

In order to play the games, the script of "MainGame.py" should be started.
This script will ask for user's name and his game choice, afterwards he will be asked for a game difficulty level as well.

In this project, in all option questions, such as choosing a game number or a difficulty level (also a number), the project will not accept any other type besided an integer - thanks to "InputNumbersOnly.py".



----MySQL (DB) & Docker----
Whenever the user wins a game, the score he gets, will be saved into a container of MySQL DB.
Which is at the same time, there is a flask python script running (MainScores.py) that displays the score in the Web.

I created 2 Dockerfiles:
1. "Dockerfile_db"
