pipeline {
    agent any
    triggers { 
        pollSCM('* * * * *') 
    } 
    stages {
        stage('First Stage') {
            steps {
                echo 'Hello world!' 
            }
        }
    }
}
