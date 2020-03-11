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

Whenever the user wins a game, the score he gets, will be stored into a container of MySQL DB using the "Scores.py" script.
Which is at the same time, there is a flask python script running (MainScores.py) that queries the DB above for the current score.
Then displays it in its web application, which can be accessed by "http://localhost:8777".


THe following were done in order to acomplish that:

I created 2 Dockerfiles:

1. Dockerfile_db - this file creates an image of "mysql" and also starts a script of "create_db_and_table.sql".
This script create a DB and a table.

2. Dockerfile_app - this file creates an image of "python" and runs a script named "MainScores.py".
As described above, this script create a web application using flask, and also queries the DB for the current score to display (using HTML) in the web.


In order to build, start and run Dockerfiles, I created a docker-compose - "docker-compose.yml".
It builds the Dockerfiles, names the new images, gives a password to the container of DB and exposes both the new containers.




----Jenkins----

The "Jenkinsfile" has a Declarative Pipeline script, that does the following:

1. Cloning the "WorldOfGames" repository into a host.
2. Builds the "docker-compose.yml".
3. Runs the "docker-compose.yml".
4. Tests (using Selenium in the script of "tests/e2e.py") the web application that the score there is within the score range specified in the script.
5. Stops and removes the containers, then pushes the built images to Dokcer-Hub.
