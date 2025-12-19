pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "saifudheenpv"
        BACKEND_IMAGE  = "taskflow-backend"
        FRONTEND_IMAGE = "taskflow-frontend"
    }

    options {
        timestamps()
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Scan - Backend') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    dir('backend') {
                        sh '''
                          sonar-scanner \
                          -Dsonar.projectKey=taskflow-backend \
                          -Dsonar.sources=. 
                        '''
                    }
                }
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

        stage('Trivy Scan - Backend') {
            steps {
                sh '''
                  trivy image --severity HIGH,CRITICAL --exit-code 1 \
                  $DOCKERHUB_USER/$BACKEND_IMAGE:latest
                '''
            }
        }

        stage('Trivy Scan - Frontend') {
            steps {
                sh '''
                  trivy image --severity HIGH,CRITICAL --exit-code 1 \
                  $DOCKERHUB_USER/$FRONTEND_IMAGE:latest
                '''
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
                sh '''
                  docker push $DOCKERHUB_USER/$BACKEND_IMAGE:latest
                  docker push $DOCKERHUB_USER/$FRONTEND_IMAGE:latest
                '''
            }
        }
    }

    post {
        success {
            echo "CI + Quality + Security pipeline SUCCESS"
        }
        failure {
            echo "Pipeline FAILED due to quality or security issues"
        }
    }
}
