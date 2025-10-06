output "repository_name" {
  description = "Nombre del repositorio ECR"
  value       = aws_ecr_repository.this.name
}

output "repository_url" {
  description = "URL completa del repositorio ECR"
  value       = aws_ecr_repository.this.repository_url
}

output "registry_id" {
  description = "ID del registro (cuenta)"
  value       = aws_ecr_repository.this.registry_id
}