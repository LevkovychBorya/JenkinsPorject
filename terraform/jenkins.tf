provider "aws" {}

resource "aws_instance" "jenkins" {
    ami = var.ami
    instance_type = "t2.micro"
    vpc_security_group_ids = [aws_security_group.TerraformSG.id]
    key_name = aws_key_pair.ssh_key.key_name
    root_block_device {
      volume_type = "gp2"
      volume_size = "8"
      delete_on_termination = true
  }
    tags = {
        Name = "JenkinsJava"
    }
  provisioner "local-exec" {
    command = "echo ${aws_instance.jenkins.public_ip} > jenkins_public_ip"
  }
}

resource "aws_security_group" "TerraformSG" {
  name = "HTTP/SSH/8080 SG"
  description = "This security group created for DockerWP"
  dynamic "ingress" {
    for_each = ["80","8080","22"]
    content {
      from_port = ingress.value
      to_port = ingress.value
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "ssh_key" {
  key_name   = "sshkey"
  public_key = file("../sshkey.pub")
}


variable "ami" {
  default = "ami-0b418580298265d5c"
} 

