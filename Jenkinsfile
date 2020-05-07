pipeline {
    agent any
    triggers { 
        pollSCM('H/2 * * * *') 
    } 
    stages {
        stage('First Stage') {
            steps {
                echo 'Hello world!' 
            }
        }
    }
}
