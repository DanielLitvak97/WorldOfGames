pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                bat "git clone https://github.com/DanielLitvak97/WorldOfGames.git"
            }
        }
        stage('Build') {
            steps {
                bat "docker-compose build"
            }  
        }
        stage('Run') {
            steps {
                bat "docker-compose up -d"
            }
        }
        stage('Test') {
            steps {
                bat "cd tests" {
                    bat 'python -c "import e2e; e2e.main_function()"'
                }
            }
        }
        stage('Finalize') {
            steps {
                bat "docker-compose down"
                bat "docker-compose push"
            } 
        }   
    }   
}


