pipeline {
    agent any
    
    environment {
        // Docker Hub credentials (configure in Jenkins credentials)
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        // Docker image details
        DOCKER_IMAGE = 'yourusername/scientific-calculator'
        DOCKER_TAG = "${BUILD_NUMBER}"
        DOCKER_LATEST = "${DOCKER_IMAGE}:latest"
        DOCKER_VERSIONED = "${DOCKER_IMAGE}:${DOCKER_TAG}"
    }
    
    tools {
        // Configure Python (ensure Python plugin is installed)
        // Adjust version based on your Jenkins configuration
        python 'Python3'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
                
                // Display repository information
                sh '''
                    echo "Repository: ${GIT_URL}"
                    echo "Branch: ${GIT_BRANCH}"
                    echo "Commit: ${GIT_COMMIT}"
                '''
            }
        }
        
        stage('Environment Setup') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    python3 --version
                    pip3 --version
                    
                    # Create virtual environment
                    python3 -m venv venv
                    . venv/bin/activate
                    
                    # Upgrade pip and install dependencies
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    
                    # List installed packages
                    pip list
                '''
            }
        }
        
        stage('Code Quality Check') {
            parallel {
                stage('Linting') {
                    steps {
                        echo 'Running code linting...'
                        sh '''
                            . venv/bin/activate
                            flake8 calculator.py test_calculator.py || true
                        '''
                    }
                }
                
                stage('Type Checking') {
                    steps {
                        echo 'Running type checking...'
                        sh '''
                            . venv/bin/activate
                            mypy calculator.py || true
                        '''
                    }
                }
            }
        }
        
        stage('Unit Testing') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    . venv/bin/activate
                    
                    # Run tests with coverage
                    python -m pytest test_calculator.py -v --tb=short
                    
                    # Alternative: Run with unittest
                    # python test_calculator.py
                    
                    echo "Unit tests completed successfully!"
                '''
            }
            post {
                always {
                    // Archive test results if using pytest-junit
                    // junit 'test-results.xml'
                    echo 'Test stage completed'
                }
            }
        }
        
        stage('Build Application') {
            steps {
                echo 'Building application...'
                sh '''
                    . venv/bin/activate
                    
                    # Compile Python files (optional)
                    python -m py_compile calculator.py
                    python -m py_compile test_calculator.py
                    
                    echo "Application built successfully!"
                '''
            }
        }
        
        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                script {
                    // Build Docker image
                    def dockerImage = docker.build("${DOCKER_IMAGE}:${BUILD_NUMBER}")
                    
                    // Tag as latest
                    sh "docker tag ${DOCKER_VERSIONED} ${DOCKER_LATEST}"
                    
                    echo "Docker image built: ${DOCKER_VERSIONED}"
                }
            }
        }
        
        stage('Docker Test') {
            steps {
                echo 'Testing Docker image...'
                sh '''
                    # Test if container runs successfully
                    docker run --rm ${DOCKER_VERSIONED} python test_calculator.py
                    
                    # Test health check
                    docker run --rm ${DOCKER_VERSIONED} python -c "from calculator import ScientificCalculator; calc = ScientificCalculator(); print('Docker test passed')"
                '''
            }
        }
        
        stage('Push to Docker Hub') {
            when {
                branch 'main'  // Only push from main branch
            }
            steps {
                echo 'Pushing to Docker Hub...'
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        // Push versioned image
                        sh "docker push ${DOCKER_VERSIONED}"
                        // Push latest tag
                        sh "docker push ${DOCKER_LATEST}"
                    }
                }
                echo "Docker images pushed successfully!"
            }
        }
        
        stage('Trigger Deployment') {
            when {
                branch 'main'
            }
            steps {
                echo 'Triggering deployment...'
                
                // Create deployment trigger file
                sh '''
                    echo "BUILD_NUMBER=${BUILD_NUMBER}" > deployment.properties
                    echo "DOCKER_IMAGE=${DOCKER_VERSIONED}" >> deployment.properties
                    echo "TIMESTAMP=$(date)" >> deployment.properties
                '''
                
                // Archive deployment properties
                archiveArtifacts artifacts: 'deployment.properties', allowEmptyArchive: false
                
                // Trigger Ansible deployment (if configured)
                // build job: 'deploy-calculator', parameters: [
                //     string(name: 'DOCKER_IMAGE', value: "${DOCKER_VERSIONED}"),
                //     string(name: 'BUILD_NUMBER', value: "${BUILD_NUMBER}")
                // ]
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed'
            
            // Clean up Docker images to save space
            sh '''
                # Remove built images (keep latest for caching)
                docker rmi ${DOCKER_VERSIONED} || true
                
                # Clean up dangling images
                docker image prune -f || true
            '''
        }
        
        success {
            echo 'Pipeline completed successfully!'
            
            // Send success notification (configure as needed)
            // emailext (
            //     subject: "Build Success: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
            //     body: "Build completed successfully. Docker image: ${DOCKER_VERSIONED}",
            //     to: "${env.CHANGE_AUTHOR_EMAIL}"
            // )
        }
        
        failure {
            echo 'Pipeline failed!'
            
            // Send failure notification
            // emailext (
            //     subject: "Build Failed: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
            //     body: "Build failed. Please check the logs.",
            //     to: "${env.CHANGE_AUTHOR_EMAIL}"
            // )
        }
        
        cleanup {
            // Clean up workspace
            sh '''
                # Remove virtual environment
                rm -rf venv || true
                
                # Clean up any temporary files
                find . -name "*.pyc" -delete || true
                find . -name "__pycache__" -type d -exec rm -rf {} + || true
            '''
        }
    }
}