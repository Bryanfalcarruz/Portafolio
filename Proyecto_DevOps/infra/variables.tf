variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}

variable "aws_profile" {
  description = "AWS CLI profile to use"
  type        = string
  default     = "bryanf606"
}

variable "project_name" {
  description = "Project tag/name"
  type        = string
  default     = "file-organizer"
}

variable "env" {
  description = "Environment (workspace)"
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR for the public subnet"
  type        = string
  default     = "10.0.1.0/24"
}

variable "tags" {
  description = "Common tags"
  type        = map(string)
  default = {
    Owner   = "Bryan Alcarruz"
    Project = "FileOrganizer"
    Managed = "Terraform"
  }
}