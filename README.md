# WorldOfGames
My DevOps Course Project:

----Python----

II created several games using python scripts.

The games:
1. CurrencyRouletteGame.py
2. GuessGame.py
3. MemoryGame.py

In order to play the games, the script of "MainGame.py" should be started.
This script will ask for user's name and his game choice, afterwards he will be asked for a game difficulty level as well.

In this project, in all option questions, such as choosing a game number or a difficulty level (also a number), the project will not accept any other type besides an integer - thanks to "InputNumbersOnly.py".




----MySQL (DB) & Docker----

Whenever the user wins a game, the score he gets, is stored into a container of DB MySQL using the "Scores.py" script.
This container is queried by another container of Python image which runs a Flask Script (MainScores.py). The query, which is for getting the current user’s score, happens when the Web Application (the Flask Script) receives a HTTP GET request. Once it gets the current score, it displays it in its Web, which can be accessed by "http://localhost:8777".


The following were done in order to accomplish that:

I created 2 Dockerfiles:

1. Dockerfile_db - this file creates an image of "MySQL" and also runs a script of "create_db_and_table.sql".
This script creates a DB and a table.

2. Dockerfile_app - this file creates an image of "Python" and runs a Script named "MainScores.py".
As described above, this script create a Web Application using Flask, and also queries the DB for the current score to display (using HTML) in the Web.


In order to build the Dockerfiles and run the relevant containers with their images, I created a docker-compose - "docker-compose.yml".
It builds the Dockerfiles, names the new images, gives a password to the container of DB and exposes both the new containers.




----Jenkins----

The "Jenkinsfile" has a Declarative Pipeline script, that does the following:

1. Cloning the "WorldOfGames" repository into a host.
2. Builds the "docker-compose.yml".
3. Runs the "docker-compose.yml".
4. Tests (using Selenium in the script of "/tests/e2e.py") the web application that the score there is within the score range specified in the script.
5. Stops and removes the containers, then pushes the built images to Dokcer-Hub.




----Kubernetes & Helm----

 This section is an alternative for those who don't want to use Docker.
 The Kubernetes Cluster uses the 2 Docker images I created above, it fetches them from "Docker Hub".
 And start and run them all. 
 
The following were done in order to accomplish that:

1. I created an "app-deployment.yaml" which creates a pod of the App (Flask Script).
2. I created an "app-service.yaml" which exposes (using NodePort) the app for outside the Kubernetes Cluster.
3. I created an "db-deployment.yaml" which creates a pod of the DB (MySQL) with a root password and port.
4. I created an "db-service.yaml" which exposes (using NodePort) the DB for outside the Kubernetes Cluster, and since it's NodePort it      allows us automatically use the Service of ClusterIP, which we need since the App has to query the DB.

Using "Helm" I packed all those files, created a "values.yaml", which allows the users to deploy those pods with customized Replicas and Services.
