pipeline {
    agent docker
    stages {
        stage('Checkout') { 
            steps {
                bat "git 'https://github.com/DanielLitvak97/WorldOfGames.git'"
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
                
}



dir('C:\\Users\\User\\AppData\\Local\\Programs\\Python\\1212121') {
                    bat 'selenium_test.py'
    
     
