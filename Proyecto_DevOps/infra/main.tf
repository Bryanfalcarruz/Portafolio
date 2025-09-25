data "aws_region" "current" {}

output "current_region" {
  value = data.aws_region.current.name
}