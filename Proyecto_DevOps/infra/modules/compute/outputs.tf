output "instance_id" {
  description = "ID de la instancia EC2 creada"
  value       = aws_instance.file_organizer_ec2.id
}

output "public_ip" {
  description = "Dirección IP pública de la instancia"
  value       = aws_instance.file_organizer_ec2.public_ip
}

output "iam_role_name" {
  description = "Nombre del rol asociado a la instancia"
  value       = aws_iam_role.ec2_role.name
}