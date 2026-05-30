provider "aws" {
    region = var.region
}

resource "aws_instance" "example" {
    ami = "ami-00263659a97a6c29c"
    instance_type = var.instance_type
}