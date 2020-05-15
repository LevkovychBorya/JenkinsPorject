pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
        disableConcurrentBuilds()
    }
    stages {
        stage('Build Stage') {
            steps {
                sh 'docker version'
            }
        }
        stage('Test Stage') {
           steps {
               echo ' this is where docker keeps jenkins work /var/lib/docker/volumes/jenkins_home/_data/workspace/JavaPipe/JavaApp'
               sh 'pwd'
           }
        }
        stage('Deploy Stage') {
           steps {
               sh 'ls -a'
           }
        }
    }
}