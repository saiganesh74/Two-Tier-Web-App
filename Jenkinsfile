pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/saiganesh74/Two-Tier-Web-App/'
            }
        }

        stage('Build & Deploy') {
    steps {
        sh '''
        docker compose down --remove-orphans || true
        docker rm -f $(docker ps -aq) || true
        docker compose up -d --build
        '''
    }
}

        stage('Verify') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
