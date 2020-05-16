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
				sh 'pwd'
				sh 'ls'
				sh 'echo ""$(pwd)"" '
				sh 'echo "\$(pwd)" '
				sh 'echo "$(!pwd)" '
				sh 'echo "${pwd}" '
				sh "echo '\$(pwd)' "
		     // sh "echo '${pwd}' "
			 // sh "echo '$(!pwd)' "
                sh 'docker run -it --rm --name maven -v "\$(pwd)":/var/lib/docker/volumes/jenkins_home/_data/workspace/JavaPipe -w /var/lib/docker/volumes/jenkins_home/_data/workspace/JavaPipe maven:3.3-jdk-8 mvn build'
            }
        }
		stage('Package Stage') {
            steps {
                sh 'docker run -it --rm --name maven -v "\$(pwd)":/var/lib/docker/volumes/jenkins_home/_data/workspace/JavaPipe -w /var/lib/docker/volumes/jenkins_home/_data/workspace/JavaPipe maven:3.3-jdk-8 mvn package'
            }
		}
		stage('Create Stage') {
            steps {
                sh 'docker run --name tomcat -d -p 80:8080 tomcat:9.0'
            }
		}
        stage('Deploy Stage') {
            steps {
				sh 'docker cp /var/lib/docker/volumes/jenkins_home/_data/workspace/JavaPipe/target/SampleServlet.war tomcat:/usr/local/tomcat/webapps'			
			}
		}
 
    }
}
