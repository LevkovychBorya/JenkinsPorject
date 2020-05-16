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
        stage('Compile Stage') {
            steps {
				sh 'sudo apt-get update'
				sh 'sudo apt-get install maven -y'
                sh 'rm -rf /JavaPipe'
				sh 'cp -r /var/jenkins_home/workspace/JavaPipe /JavaPipe'
				sh 'cd /JavaPipe && mvn compile '
            }
        }
		stage('Package Stage') {
            steps {
                sh 'cd /JavaPipe && mvn package'
            }
		}
        stage('Deploy Stage') {
            steps {
				sh '[ ! "$(docker ps -a | grep tomcat)" ] && docker run --name tomcat -d -p 80:8080 tomcat:9.0'
				sh 'docker exec tomcat rm -rf /usr/local/tomcat/webapps/'	
				sh 'docker cp /JavaPipe/target/SampleServlet.war tomcat:/usr/local/tomcat/webapps'			
			}
		}
 
    }
}
