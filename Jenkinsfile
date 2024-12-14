pipeline {
    agent any
    environment {
        GIT_CREDENTIALS = 'gh-tkn' // Replace with your credential ID
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
    }
} 
