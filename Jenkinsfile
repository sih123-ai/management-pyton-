pipeline {
    agent any
    tools {
        maven 'Maven 3.8.1'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/sih123-ai/management-pyton-.git', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Make sure the full path to python3 and pip3 is used or activate virtual environment
                    try {
                        sh '/path/to/python3 -m pip install -r requirements.txt' // Adjust this path
                    } catch (Exception e) {
                        echo "Failed to install dependencies: ${e}"
                        throw e
                    }
                }
            }
        }
        stage('Test Application') {
            steps {
                script {
                    // Ensure pytest is installed and available in the environment
                    try {
                        sh '/path/to/python3 -m pytest tests' // Adjust this path if necessary
                    } catch (Exception e) {
                        echo "Tests failed: ${e}"
                        throw e
                    }
                }
            }
        }
        stage('Build with Maven') {
            steps {
                script {
                    try {
                        // Use Maven to build the project
                        sh 'mvn clean install'
                    } catch (Exception e) {
                        echo "Maven build failed: ${e}"
                        throw e
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'Build and execution completed successfully!'
        }
        failure {
            echo 'The build or execution failed. Check the logs for details.'
        }
    }
}
