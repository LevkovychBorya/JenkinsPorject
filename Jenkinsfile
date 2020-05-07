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
        stage('First Stage') {
            steps {
                echo 'Hello world!' 
            }
        }
    }
}
#hello
