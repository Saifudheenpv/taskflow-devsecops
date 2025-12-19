pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "saifudheenpv"
        BACKEND_IMAGE  = "taskflow-backend"
        FRONTEND_IMAGE = "taskflow-frontend"
    }

    options {
        timestamps()
        ansiColor('xterm')
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
                    sh '''
                        docker build -t $DOCKERHUB_USER/$BACKEND_IMAGE:latest .
                    '''
                }
            }
        }

        stage('Build Frontend Image') {
            steps {
                dir('frontend') {
                    sh '''
                        docker build -t $DOCKERHUB_USER/$FRONTEND_IMAGE:latest .
                    '''
                }
            }
        }

        stage('Trivy Scan - Backend Image') {
            steps {
                sh '''
                    echo "🔍 Scanning backend image with Trivy"
                    trivy image \
                      --severity HIGH,CRITICAL \
                      --exit-code 1 \
                      $DOCKERHUB_USER/$BACKEND_IMAGE:latest
                '''
            }
        }

        stage('Trivy Scan - Frontend Image') {
            steps {
                sh '''
                    echo "🔍 Scanning frontend image with Trivy"
                    trivy image \
                      --severity HIGH,CRITICAL \
                      --exit-code 1 \
                      $DOCKERHUB_USER/$FRONTEND_IMAGE:latest
                '''
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Images to Docker Hub') {
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
            echo "✅ CI + Trivy pipeline completed successfully"
        }
        failure {
            echo "❌ Pipeline failed (Security or Build issue)"
        }
        always {
            sh 'docker logout || true'
        }
    }
}
