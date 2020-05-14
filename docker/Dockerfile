
FROM jenkins/jenkins
 
USER root
RUN apt-get update \
      && apt-get install -y sudo \
      && rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

RUN /usr/local/bin/install-plugins.sh git matrix-auth workflow-aggregator docker-workflow credentials-binding scm-api git-client greenballs 

ENV JENKINS_USER=admin
ENV JENKINS_PASS=admin

ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false


COPY default-user.groovy /usr/share/jenkins/ref/init.groovy.d/
