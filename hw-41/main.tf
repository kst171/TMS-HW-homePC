terraform {
  backend "s3" {
    bucket         = "kst-terraform-state-hw"  
    key            = "dev/terraform.tfstate" # Путь, где будет лежать файл в бакете
    region         = "eu-north-1"
    use_lockfile   = true                    # Включаем современную нативную блокировку в S3 вместо DynamoDB
    encrypt        = true                    # Включает шифрование при передаче
  }
}

provider "aws" {
  region  = var.region
}

# Вызов модуля для Web-сервера
module "web_server" {
  source        = "./modules/aws_ec2"
  
  # Передаем параметры внутрь модуля
  instance_type = "t3.micro"
  instance_name = "KST-Web-Prod"
}

# Мы можем вызвать этот же модуль второй раз одной строчкой для другого сервера!
module "db_server" {
  source        = "./modules/aws_ec2"
  
  instance_type = "t3.small"
  instance_name = "KST-DB-Prod"
}

# Чтобы вывести IP-адрес в терминал после apply
output "web_public_ip" {
  value = module.web_server.public_ip
}
