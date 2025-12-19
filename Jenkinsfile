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

        /* =======================
           1. CHECKOUT SOURCE CODE
           ======================= */
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        /* =======================
           2. SONARQUBE CODE SCAN
           ======================= */
        stage('SonarQube Scan - Backend') {
            environment {
                SCANNER_HOME = tool 'Sonar-Scanner'
            }
            steps {
                withSonarQubeEnv('SonarQube') {
                    dir('backend') {
                        sh '''
                          $SCANNER_HOME/bin/sonar-scanner \
                          -Dsonar.projectKey=taskflow-backend \
                          -Dsonar.projectName=TaskFlow-Backend \
                          -Dsonar.sources=. \
                          -Dsonar.language=py
                        '''
                    }
                }
            }
        }

        /* =======================
           3. BUILD BACKEND IMAGE
           ======================= */
        stage('Build Backend Image') {
            steps {
                dir('backend') {
                    sh '''
                      docker build -t $DOCKERHUB_USER/$BACKEND_IMAGE:latest .
                    '''
                }
            }
        }

        /* =======================
           4. BUILD FRONTEND IMAGE
           ======================= */
        stage('Build Frontend Image') {
            steps {
                dir('frontend') {
                    sh '''
                      docker build -t $DOCKERHUB_USER/$FRONTEND_IMAGE:latest .
                    '''
                }
            }
        }

        /* =======================
           5. TRIVY SECURITY SCAN
           ======================= */
        stage('Trivy Scan - Backend Image') {
            steps {
                sh '''
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
                  trivy image \
                  --severity HIGH,CRITICAL \
                  --exit-code 1 \
                  $DOCKERHUB_USER/$FRONTEND_IMAGE:latest
                '''
            }
        }

        /* =======================
           6. DOCKER LOGIN
           ======================= */
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

        /* =======================
           7. PUSH IMAGES
           ======================= */
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
            echo "✅ CI + SonarQube + Trivy pipeline SUCCESSFUL"
        }
        failure {
            echo "❌ Pipeline FAILED (Quality or Security gate)"
        }
        always {
            sh 'docker logout || true'
        }
    }
}
