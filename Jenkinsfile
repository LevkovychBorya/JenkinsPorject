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
                echo 'Here Maven is going to build Java application.'
            }
        }
        stage('Test Stage') {
           steps {
               echo 'Here Maven is going to Test Java application.'
           }
        }
        stage('Deploy Stage') {
           steps {
               sh 'pwd'
               //sh ''
               sh ' ssh -i /home/ubuntu/.ssh/ssh.pem ubuntu@172.17.0.3 rm -rf webapps/JavaApp'
               sh ' ssh -i /home/ubuntu/.ssh/ssh.pem ubuntu@172.17.0.3 rm -rf webapps/JavaApp.war'
               sh ' scp -i /home/ubuntu/.ssh/ssh.pem -r JavaApp ubuntu@172.17.0.3:webapps/'
           }
        }
    }
}
