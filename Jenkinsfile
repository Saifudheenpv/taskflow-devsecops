pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "saifudheenpv"
        BACKEND_IMAGE  = "taskflow-backend"
        FRONTEND_IMAGE = "taskflow-frontend"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Backend Image') {
            steps {
                dir('backend') {
                    sh 'docker build -t $DOCKERHUB_USER/$BACKEND_IMAGE:latest .'
                }
            }
        }

        stage('Build Frontend Image') {
            steps {
                dir('frontend') {
                    sh 'docker build -t $DOCKERHUB_USER/$FRONTEND_IMAGE:latest .'
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Images') {
            steps {
                sh 'docker push $DOCKERHUB_USER/$BACKEND_IMAGE:latest'
                sh 'docker push $DOCKERHUB_USER/$FRONTEND_IMAGE:latest'
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully'
        }
        failure {
            echo 'CI Pipeline failed'
        }
    }
}
