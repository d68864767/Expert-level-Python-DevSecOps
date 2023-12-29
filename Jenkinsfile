pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'docker build -t python-app .'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'docker run --rm python-app python test_main.py'
            }
        }
        stage('Security Test') {
            steps {
                echo 'Security Testing..'
                sh 'docker run --rm python-app python security_tests.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'docker run -d -p 5000:5000 python-app'
            }
        }
    }
}
