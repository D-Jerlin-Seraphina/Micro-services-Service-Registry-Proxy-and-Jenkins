pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building Service A...'
                sh 'docker build -t service-a service-a'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying Service A...'
                sh 'sh deploy.sh'
            }
        }
        
        stage('Verify') {
            steps {
                echo 'Verifying deployment...'
                sh 'docker ps | grep service-a'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
