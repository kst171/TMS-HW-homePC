variable "instance_type" {
  description = "Тип инстанса EC2"
  default     = "t2.micro"
}

variable "instance_name" {
  description = "Значение тега Name для сервера"
}

variable "ami_id" {
  description = "ID образа AMI"
  default     = "ami-067bcf851477ebb78" # Ubuntu 24.04
}