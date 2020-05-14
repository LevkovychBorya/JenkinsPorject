# Aw **** here we go again.
In this project Terraform is going to take pregenerated python's ssh key, create security group and instance. Python script using paramiko module is going to download docker.io, transfer Dockerfile and groovy-script on remote instance then build a image and run it as a container. After that python is going to fetch jenkins-cli.jar from that container and create a job with changed inside githuburl, branch and script path that is needed to create a pipeline from github to this instance. After that you will have fully-functioning Jenkins-server that you can acess to with username and password that you choose as an arguments. Also jenkins have full acess to docker on that instance.

The example of repository that is going to be used for pipeline is on the Java branch.

To run the script you need to create aws user with secret key, have terraform, java and python, install paramiko module and own a user that can run terraform.

Command to run the script: python setup.py << AWS_ACCESS_KEY_ID >> << AWS_SECRET_ACCESS_KEY >> << AWS_DEFAULT_REGION >> << GITHUB_URL >>
<< BRANCH >> << SCRIPT_PATH >> << USERNAME >> << PASSWORD >>

Script is going to print out every output and also containers id's so you know they actually running. And when it's done its going to say so 👌.
