pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '1'))
        disableConcurrentBuilds()
    }
    stages {
        stage('Build Stage') {
            steps {
                echo 'Here Maven is going to build Java application.'
            }
        }
        stage('Test Stage') {
           steps {
               echo 'Here Maven is going to Test Java application.'
           }
        }
        stage('Test Stage') {
           steps {
               echo 'Here Maven is going to Test Java application.'
           }
        }
    }
}
