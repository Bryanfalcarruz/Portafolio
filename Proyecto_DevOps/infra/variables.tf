variable "aws_region" {
  type        = string
  description = "Región AWS a usar"
  default     = "us-west-2"  # Oregon
}

variable "aws_profile" {
  type        = string
  description = "Nombre del perfil de AWS CLI a usar (aws configure --profile ...)"
  default     = "portfolio-dev"  # cámbialo si usaste otro nombre
}

variable "project_name" {
  type        = string
  description = "Nombre base para tags y recursos"
  default     = "file-organizer"
}