# WorldOfGames

----Python----
I created several games using python scripts.

The games:
1. CurrencyRouletteGame.py
2. GuessGame.py
3. MemoryGame.py

In order to play the games, the script of "MainGame.py" should be started.
This script will ask for user's name and his game choice, afterwards he will be asked for a game difficulty level as well.

In this project, in all option questions, such as choosing a game number or a difficulty level (also a number), the project will not accept any other type besided an integer - thanks to "InputNumbersOnly.py".



----MySQL (DB) & Docker----
Whenever the user wins a game, the score he gets, will be saved into a container of MySQL DB.
Which is at the same time, there is a flask python script running (MainScores.py) that queries the DB above for the current score.
Then displays it in its web application, which can be accessed by "http://localhost:8777".


THe following were done to acomplish that:

I created 2 Dockerfiles:

1. Dockerfile_db - this file creates an image of "mysql" and also starts a script of "create_db_and_table.sql".
This script create a DB and a table.

2. Dockerfile_app - this file creates an image of "python" and runs a script named "MainScores.py".
As described above, this script create a web application using flask, and also queries the DB for the current score to display (using HTML) in the web.

