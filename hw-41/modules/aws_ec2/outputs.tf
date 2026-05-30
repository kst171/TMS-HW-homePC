output "instance_id" {
  value       = aws_instance.example.id
  description = "ID созданного EC2 инстанса"
}

output "public_ip" {
  value       = aws_instance.example.public_ip
  description = "Публичный IP-адрес сервера"
}