pipeline {
    agent any
    stages {
        stage('Checkout') { 
            steps {
                dir('WorldOfGames')
            }
            steps {
                dir('WorldOfGames')
            }
        }
        stage('Build') {
           steps {
                bat "docker-compose build"
           }  
        }
        stage('Run'){
            steps {
                bat 'docker-compose up'
            }
        }
        stage('Test') {
            steps {
                bat "python -c 'import e2e; print e2e.main_function()'"
            }
        } 
    }   
}


