pipeline {
	agent any
	environment {
		CREDENTIALS = credentials('dkr0')
		GIT_CREDENTIALS = 'gh-tkn' // Replace with your credential ID
		DOCKER_IMG = 'zdev19/z3-server:latest'
	}
	stages {
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
		stage('build img') {
			steps {
				sh 'docker --version'
				sh 'docker build --platform=linux/amd64 -t zdev19/z3-server:latest .'
			}
		}
		stage('login') {
			steps {
				sh 'echo $CREDENTIALS_PSW | docker login -u $CREDENTIALS_USR --password-stdir'
			}
		}
		stage('push img') {
			steps {
				sh 'docker push $DOCKER_IMG'
			}
		}
	}
	post {
		always {
			sh 'docker logout'
		}
		success {
			echo 'Image built and pushed successfully'
		}
		failure {
			echo 'Failed to build or push image'
		}
	}
}
