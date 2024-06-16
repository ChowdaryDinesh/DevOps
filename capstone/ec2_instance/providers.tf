terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.53.0"
    }
  }
}

provider "aws" {
  region     = var.aws_region
  access_key = ""
  secret_key = ""
  token = ""
   
}
