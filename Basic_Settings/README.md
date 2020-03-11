# WorldOfGames

----Python----

I created several games using python scripts.

The games:
1. CurrencyRouletteGame.py
2. GuessGame.py
3. MemoryGame.py

In order to play the games, the script of "MainGame.py" should be started. This script will ask for user's name and his game choice, afterwards he will be asked for a game difficulty level as well.

In this project, in all option questions, such as choosing a game number or a difficulty level (also a number), the project will not accept any other type besided an integer - thanks to "InputNumbersOnly.py".

----Python - Files I/O & Docker------

Whenever the user wins a game, the score he gets, will be stored into a "Scores.txt" file using "Scores.py" script. Which is at the same time, there is a flask python script running (MainScores.py) inside a container, that has this file mounted from the host to the container's root directoty. Then the flask displays it in its web application, which can be accessed by "http://localhost:8777".

The following were done in order to accomplish that:

1. Dockerfile - this file creates an image of "python" and runs a script named "MainScores.py". As described above, this script create a web application using flask.

2. docker-compose - In order to build the Dockerfile and run the relevant container with its images, I created a docker-compose - "docker-compose.yml". It builds the Dockerfile, names the new image, mounts the "Scores.txt" from the host to the container, and exposes both the new containers.

----Jenkins----

The "Jenkinsfile" has a Declarative Pipeline script, that does the following:

1. Cloning the "WorldOfGames" repository into a host.
2. Builds the "docker-compose.yml".
3. Runs the "docker-compose.yml".
4. Tests (using Selenium in the script of "tests/e2e.py") the web application that the score there is within the score range specified in the script.
5. Stops and removes the containers, then pushes the built images to Dokcer-Hub.
