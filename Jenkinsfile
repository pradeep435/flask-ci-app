pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository...'
                git 'https://github.com/pradeep435/flask-ci-app.git'
            }
        }

        stage('Pull Docker Image from Docker Hub') {
            steps {
                echo 'Pulling latest Docker image from Docker Hub...'
                sh 'docker pull pradeepravi022/flask-app:latest'
            }
        }

        stage('Stop and Remove Old Container') {
            steps {
                echo 'Stopping and removing any old container...'
                sh '''
                docker stop flask-app || true
                docker rm flask-app || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                echo 'Running new Docker container...'
                sh 'docker run -d --name flask-app -p 5000:5000 pradeepravi022/flask-app:latest'
            }
        }
    }
}
