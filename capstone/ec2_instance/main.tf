resource "aws_vpc" "my_vpc" {
    cidr_block = var.vpc_cidr
    instance_tenancy = "default"
    tags = {
        Name = "Instance-test"
    }
}

resource "aws_subnet" "name" {
    count = length(var.subnet_cidr)
    vpc_id = aws_vpc.my_vpc.id
    cidr_block = var.subnet_cidr[count.index]["cidr_block"]
    tags = {
        Name = var.subnet_cidr[count.index]["name"]
    }
    availability_zone = "us-east-1a"
}

resource "aws_internet_gateway" "igw1" {
    vpc_id = aws_vpc.my_vpc.id
    tags = {
        Name = "igw1"
    } 
}

resource "aws_route_table" "rt_table" {
    vpc_id = aws_vpc.my_vpc.id

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.igw1.id
    }
    tags = {
        Name = "rt_table"
    }
}

resource "aws_route_table_association" "rt_association" {
    subnet_id = aws_subnet.name[0].id
    route_table_id = aws_route_table.rt_table.id 
}

resource "aws_security_group" "sg" {
    count = length(var.subnet_cidr)
    vpc_id = aws_vpc.my_vpc.id
    tags = {
    Name = "SG_${var.subnet_cidr[count.index].name}"
  }
    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
        description = "Allow all outbound traffic"
    }
    ingress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = [var.subnet_cidr[count.index].cidr_block]
        description = "Allow all traffic from local subnet"
    }
    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    ingress {
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    ingress {
        from_port = 8000
        to_port = 8000
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    
    ingress {
        from_port = 8080
        to_port = 8080
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}


resource "aws_network_interface" "ni_1" {
    count = length(var.subnet_cidr)
    subnet_id = aws_subnet.name[count.index].id 
    security_groups = [aws_security_group.sg[0].id]
    tags = {
        Name = "ni_${var.subnet_cidr[count.index].name}"
    }
}

resource "aws_eip" "eip" {
    instance = aws_instance.ec2_instance.id
}

resource "aws_eip_association" "eipa" {
    network_interface_id = aws_network_interface.ni_1[0].id
    allocation_id = aws_eip.eip.id
}

resource "aws_key_pair" "private_key" {
    count      = var.create_new_keypair ? 1 : 0
    key_name = "key"
    public_key = file("Key1.pub")
}

resource "aws_instance" "ec2_instance" {
    instance_type = var.instance_type
    key_name = var.create_new_keypair ? aws_key_pair.private_key[0].key_name : "Key.pem"
    ami = var.ami_id
    network_interface {
        device_index = 0
        network_interface_id = aws_network_interface.ni_1[0].id
    }

    user_data = templatefile("${path.module}/${var.app}.sh", {})
    tags = {
      User = "test-user"
      Name = "test-instance-${var.app}"
      env = var.env
    }
    connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("Key.pem")
    host        = self.public_ip
  }
}
