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
                    // Install Python dependencies
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('Test Application') {
            steps {
                script {
                    // Run tests using pytest
                    sh 'pytest tests'
                }
            }
        }
        stage('Build with Maven') {
            steps {
                script {
                    // Use Maven to build the project
                    sh 'mvn clean install'
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
