pipeline {
    agent none
    triggers {
        pollSCM('* * * * *')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
        disableConcurrentBuilds()
    }
    stages {
        stage('Build Stage') {
            agent {
                docker { image 'maven:3-alpine' }
            }
            steps {
                sh 'mvn --version'
            }
        }
        stage('Test Stage') {
           steps {
               echo 'Here Maven is going to test Java application.'
           }
        }
        stage('Deploy Stage') {
           agent {
                docker { image 'tomcat:9.0' }
            }
           steps {
               sh 'ls -a'
           }
        }
    }
}
