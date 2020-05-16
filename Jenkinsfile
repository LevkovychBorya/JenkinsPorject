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
                sh "docker run --rm --name maven -v '\$(pwd)':/var/jenkins_home/workspace/JavaPipe -w /var/jenkins_home/workspace/JavaPipe maven:3.3-jdk-8 mvn build"
            }
        }
		stage('Package Stage') {
            steps {
                sh "docker run --rm --name maven -v '\$(pwd)':/home/ubuntu/JavaPipe -w /home/ubuntu/JavaPipe maven:3.3-jdk-8 mvn package"
            }
		}
		stage('Create Stage') {
            steps {
                sh 'docker run --name tomcat -d -p 80:8080 tomcat:9.0'
            }
		}
        stage('Deploy Stage') {
            steps {
				sh 'docker cp /home/ubuntu/JavaPipe/target/SampleServlet.war tomcat:/usr/local/tomcat/webapps'			
			}
		}
 
    }
}
