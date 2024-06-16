variable "aws_region" {
  default = "us-east-1"
}

variable "vpc_cidr" {
  default = "172.32.0.0/16"
}

variable "subnet_cidr" {
  default = [
    {
        "name" = "subnet1"
        "cidr_block" = "172.32.10.0/24"
    }
  ]
  }

variable "ami_id" {  
  default = "ami-080e1f13689e07408"
}

variable "instance_type" {
  default = "t2.medium"
}

variable "env" {
  default = "dev"
  
}
variable "create_new_keypair" {
  default = false
}

variable "app" {
  default = "jenkins"
}