output "vpc_id" {
  value       = module.network.vpc_id
  description = "VPC ID"
}

output "public_subnet_id" {
  value       = module.network.public_subnet_id
  description = "Public subnet ID"
}

output "sg_base_id" {
  value       = module.network.sg_base_id
  description = "Base Security Group ID"
}