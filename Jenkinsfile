pipeline {
    agent any
    environment {
        GIT_CREDENTIALS = 'gh-tkn' // Replace with your credential ID
		IMG = 'zdev19/z3-server:latest'
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']], // Ensure the branch is correct
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [],
                    userRemoteConfigs: [[
                        url: 'https://github.com/Z3DRP/z3-server.git',
                        credentialsId: GIT_CREDENTIALS
                    ]]
                ])
            }
        }
		stage('Build docker image for ubunut arch amd64') {
			sh 'docker --version'
			script {
				docker.build("${IMG}", "--platform=linux/amd64 .")
			}
		}
		stage('Publish docker image') {
			sh 'echo "not implemented"'
		}
    }
} 
