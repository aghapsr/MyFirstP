pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('mehdi/html-nginx-site')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker rm -f html-nginx || true'
                    sh 'docker run -d --name html-nginx -p 8081:80 mehdi/html-nginx-site'
                }
            }
        }
    }
}

