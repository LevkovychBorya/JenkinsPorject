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
				sh 'sudo docker cp jenkins:/var/jenkins_home/workspace/JavaPipe /home/ubuntu/JavaPipe'
                sh 'sudo docker run -it --rm --name maven -v "$(pwd)":/home/ubuntu/JavaPipe -w /home/ubuntu/JavaPipe maven:3.3-jdk-8 mvn build'
            }
        }
		stage('Package Stage') {
           steps {
               sh 'sudo docker run -it --rm --name maven -v "$(pwd)":/home/ubuntu/JavaPipe -w /home/ubuntu/JavaPipe maven:3.3-jdk-8 mvn package'
            }
		}
		stage('Create Stage') {
           steps {
               sh 'sudo docker run --name tomcat -d -p 80:8080 tomcat:9.0'
            }
		}
        stage('Deploy Stage') {
           steps {
				sh 'sudo docker cp /home/ubuntu/JavaPipe/target/SampleServlet.war tomcat:/usr/local/tomcat/webapps'			
			}
		}
 
    }
}
