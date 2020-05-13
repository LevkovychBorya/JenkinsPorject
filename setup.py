import os, sys, paramiko, time, getpass, urllib.request

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
    time.sleep(60)

def ConfiguringInstance():
    publicip = open("terraform/jenkins_public_ip", "r").read()
    publicip = publicip.rstrip('\n')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=publicip, username='ubuntu', key_filename='sshkey')

    stdin, stdout, stderr = client.exec_command('sudo apt-get update')
    print(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = client.exec_command('sudo apt-get install docker.io -y')
    print(stdout.read().decode('utf-8'))

    ftp_client = client.open_sftp()
    ftp_client.put("docker/Dockerfile", "Dockerfile")
    stdin, stdout, stderr = client.exec_command('sudo docker build -t myjenkins .')
    print(stdout.read().decode('utf-8'))
    stdin, stdout, stderr = client.exec_command('sudo rm -rf Dockerfile')
    print(stdout.read().decode('utf-8'))
    ftp_client.close()

    stdin, stdout, stderr = client.exec_command('sudo docker container ls -a')
    if "jenkins" in stdout.read().decode('utf-8'):
        print("Jenkins already exist\n")
    else:
        stdin, stdout, stderr = client.exec_command('sudo docker run --name jenkins -d -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker -v jenkins_home:/var/jenkins_home -p 8080:8080 myjenkins')
        print(stdout.read().decode('utf-8'))

    client.close()

def Jenkins():
    publicip = open("terraform/jenkins_public_ip", "r").read()
    publicip = publicip.rstrip('\n')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=publicip, username='ubuntu', key_filename='sshkey')

    while True:
        if os.path.isfile('jenkins-cli.jar'):
            break
        else:
            try:
                url = 'http://' + publicip + ':8080/jnlpJars/jenkins-cli.jar'
                urllib.request.urlretrieve(url, "jenkins-cli.jar")
                print("jenkins-cli.jar was downloaded\n")
                break
            except (urllib.request.URLError, urllib.request.HTTPError, ConnectionRefusedError, ValueError) as e:
                continue

    stdin, stdout, stderr = client.exec_command('sudo docker exec jenkins ls /var/jenkins_home/secrets')
    if "initialAdminPassword" in stdout.read().decode('utf-8'):
        print("Now go to this url and unlock Jenkins: http://" + publicip + ":8080\n")
        stdin, stdout, stderr = client.exec_command('sudo docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword')
        print("Use this administrator password to unlock Jenkins: " + stdout.read().decode('utf-8') + "\n")
    else:
        print("Jenkins is already unlocked\n")

    while True:
        login = input("Please input your Jenkins username : ")
        password = getpass.getpass(prompt='And password: ')
        if "Authenticated" in os.popen('sudo java -jar jenkins-cli.jar -auth ' + login + ':' + password + ' -s http://' + publicip + ':8080 who-am-i').read():
            break
        else:
            print("\nWrong username or password try again\n")
            continue

    while True:
        githuburl = input("Please input your github repository URL : ")
        githubbranch = input("Branch name (Nothing for master) : ") or "master"
        scriptpath = input("And script path (Nothing for Jenkinsfile) : ") or "Jenkinsfile"

        try:
            request = urllib.request.Request(githuburl + "/tree/" + githubbranch + "/" + scriptpath)
            request.get_method = lambda: 'HEAD'
            urllib.request.urlopen(request)
            conf = open("Job.xml", "r")
            list_of_lines = conf.readlines()
            list_of_lines[11] = "          <url>" + githuburl + "</url>\n"
            list_of_lines[16] = "          <name>*/" + githubbranch + "</name>\n"
            list_of_lines[23] = "    <scriptPath>" + scriptpath + "</scriptPath>\n"
            conf = open("Job.xml", "w")
            conf.writelines(list_of_lines)
            conf.close()
            break
        except (urllib.request.URLError, urllib.request.HTTPError, ValueError) as e:
            print("\nThere is no such url or branch or script path! Try again\n")
            continue

    if "JavaPipe" in os.popen('sudo java -jar jenkins-cli.jar -auth ' + login + ':' + password + ' -s http://' + publicip + ':8080 list-jobs').read():
        os.system('sudo java -jar jenkins-cli.jar -auth ' + login + ':' + password + ' -s http://' + publicip + ':8080 update-job JavaPipe < Job.xml')
    else:
        os.system('sudo java -jar jenkins-cli.jar -auth ' + login + ':' + password + ' -s http://' + publicip + ':8080 create-job JavaPipe < Job.xml')
    os.system('sudo java -jar jenkins-cli.jar -auth ' + login + ':' + password + ' -s http://' + publicip + ':8080 build JavaPipe')

    print("\nDone! Pipeline was created and built!")

#
Terraform()
ConfiguringInstance()
Jenkins()
