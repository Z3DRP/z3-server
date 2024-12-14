pipeline {
	agent any
	tools {
		git 'Default'
	}
	environment {
		CREDENTIALS = credentials('dkr0')
		DOCKER_IMG = 'zdev19/z3-server:latest'
	}
	stages {
		stage('checkout code') {
			steps {
				git branch: 'main', credentialsId: 'gh-tkn', url: 'https://github.com/Z3DRP/z3-server.git'
			}
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
