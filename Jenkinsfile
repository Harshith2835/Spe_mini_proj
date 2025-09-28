pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "harsh2835/spe_mini_project"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
    }

    stages {
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh 'pip install -r requirements.txt'
                sh 'python3 -m unittest test_calculator.py'
            }
        }

        stage('Build and Tag Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                sh "docker build -t ${DOCKER_IMAGE}:${env.BUILD_NUMBER} ."
                sh "docker tag ${DOCKER_IMAGE}:${env.BUILD_NUMBER} ${DOCKER_IMAGE}:latest"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Logging in and pushing image...'
                sh "docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}"
                sh "docker push ${DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                sh "docker push ${DOCKER_IMAGE}:latest"
            }
        }

        stage('Deploy with Ansible') {
            steps {
                echo 'Deploying application...'
                sh 'ansible-playbook deploy.yml'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Sending email...'
            emailext (
                to: 'harshithr693@gmail.com',
                subject: "Jenkins Build: ${currentBuild.currentResult} - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """<p>Check console output at <a href="${env.BUILD_URL}">${env.JOB_NAME} [ #${env.BUILD_NUMBER} ]</a></p>
                       <p>Project: ${env.JOB_NAME}</p>
                       <p>Build Number: ${env.BUILD_NUMBER}</p>
                       <p>Status: ${currentBuild.currentResult}</p>
                       <p>URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>"""
            )
        }
    }
}