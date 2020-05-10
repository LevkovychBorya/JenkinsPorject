import os, sys, paramiko, time, getpass
def startup():
    os.system('sudo apt-get update')
    os.system('sudo apt-get install openjdk-8-jdk -y')
    os.system('sudo apt-get install unzip -y')
    if "Terraform" in os.popen('terraform -v').read():
        print("\nYou have already installed terraform\n")
    else:
        os.system('sudo wget https://releases.hashicorp.com/terraform/0.12.24/terraform_0.12.24_linux_amd64.zip')
        os.system('unzip terraform_0.12.24_linux_amd64.zip')
        os.system('rm terraform_0.12.24_linux_amd64.zip')
        os.system('sudo mv terraform /bin/')
    os.system('sudo apt-get install python3-pip')
    os.system('sudo pip3 install paramiko')

def AWS():
    KeyID = sys.argv[1]
    SecretKey = sys.argv[2]
    Region = sys.argv[3]
    credentials = ('export AWS_ACCESS_KEY_ID='+KeyID+' && export AWS_SECRET_ACCESS_KEY='+SecretKey+
    ' && export AWS_DEFAULT_REGION='+Region)
    return credentials

def ssh_key():
    if os.path.isfile('sshkey'):
        print('\n'"sshkey already exists no need to create new one")
    else:
        os.system("ssh-keygen -f sshkey -q -N ''")

def Terraform():
    ssh_key()
    credentials = AWS()
    os.system(credentials + ' && cd terraform && terraform init && terraform apply -auto-approve')

def ConfiguringInstance():
    time.sleep(60)
    publicip = open("terraform/jenkins_public_ip", "r").read()
    publicip = publicip.rstrip('\n')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=publicip, username='ubuntu', key_filename='sshkey')

    stdin, stdout, stderr = client.exec_command('sudo apt-get update')
    print(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = client.exec_command('sudo apt-get install docker.io -y')
    print(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = client.exec_command('sudo apt-get install openjdk-8-jdk -y')
    print(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = client.exec_command('wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -')
    print(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = client.exec_command('sudo sh -c "echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list"')
    print(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = client.exec_command('sudo apt-get update -y')
    print(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = client.exec_command('sudo apt-get install jenkins -y')
    print(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = client.exec_command('sudo docker pull tomcat:9.0')
    print(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = client.exec_command('sudo docker pull maven')
    print(stdout.read().decode('utf-8'))

    client.close()

def Jenkins():
    publicip = open("terraform/jenkins_public_ip", "r").read()
    publicip = publicip.rstrip('\n')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=publicip, username='ubuntu', key_filename='sshkey')

    if os.path.isfile('jenkins-cli.jar'):
        print("jenkins-cli.jar exists")
    else:
        os.system('sudo wget http://' + publicip + ':8080/jnlpJars/jenkins-cli.jar')

    stdin, stdout, stderr = client.exec_command('sudo ls /var/lib/jenkins/secrets/')
    if "initialAdminPassword" in stdout.read().decode('utf-8'):
        stdin, stdout, stderr = client.exec_command('sudo cat /var/lib/jenkins/secrets/initialAdminPassword')
        print("This is administrator password: " + stdout.read().decode('utf-8') + "Use it to unlock Jenkins")
    else:
        print("Jenkins is already unlocked")

    while True:
        login = input("Please input your Jenkins username : ")
        password = getpass.getpass(prompt='And password: ')
        if "Authenticated" in os.popen('sudo java -jar jenkins-cli.jar -auth ' + login + ':' + password + ' -s http://' + publicip + ':8080 who-am-i').read():
            break
        else:
            print("Wrong username or password try again")
            continue
    print(login + password)

startup()
Terraform()
ConfiguringInstance()
Jenkins()
