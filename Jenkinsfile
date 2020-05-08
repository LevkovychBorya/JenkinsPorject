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
               sh 'sudo ssh -i /home/ubuntu/.ssh/ssh.pem ubuntu@52.28.1.54 rm -rf /opt/tomcat/webapps/JavaApp'
               sh 'sudo ssh -i /home/ubuntu/.ssh/ssh.pem ubuntu@52.28.1.54 rm -rf /opt/tomcat/webapps/JavaApp.war'
               sh 'sudo scp -i /home/ubuntu/.ssh/ssh.pem -r JavaApp ubuntu@52.28.1.54:/opt/tomcat/webapps/'
           }
        }
    }
}
