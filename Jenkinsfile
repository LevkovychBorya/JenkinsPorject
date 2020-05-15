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
                docker { image 'maven' }
            }
            steps {
                sh 'mvn --version'
            }
        }
        stage('Test Stage') {
			agent {
                docker { image 'tomcat:9.0' }
            }
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