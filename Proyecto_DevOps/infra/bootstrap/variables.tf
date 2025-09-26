Set-Content .\variables.tf @'
variable "aws_region" {
  type    = string
  default = "us-west-2"
}

variable "aws_profile" {
  type    = string
  default = "portfolio-dev"
}

variable "project_name" {
  type        = string
  default     = "file-organizer"
  description = "Prefijo para nombrar recursos del backend"
}
'@