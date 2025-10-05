output "vpc_id" {
  value       = aws_vpc.this.id
  description = "VPC ID"
}

output "public_subnet_id" {
  value       = aws_subnet.public_a.id
  description = "Public subnet (AZ A) ID"
}

output "route_table_public_id" {
  value       = aws_route_table.public.id
  description = "Public route table ID"
}

output "sg_base_id" {
  value       = aws_security_group.base.id
  description = "Base Security Group ID"
}