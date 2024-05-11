# This code deploys wordpress application on AWS
# Pre-requisites:
    1. Terraform should be installed in the system
    2. ansible should be installed in the system
    3. Get the AccessKey, SecretKey and Session/SecretToken and update in the providers.
    4. This simply deploy the instance with single interface though we have used in the loop, for now, have only one value in the variables in the subnet_cidr.

# What is does?
1. Creates a new VPC.
2. Creates a public subnet.
3. Creates an EC2 instance and update the SGs.
4. Calls the local-prov to install the wordpress using Ansible.