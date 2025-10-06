variable "project_name" {
  description = "Nombre del proyecto para etiquetado"
  type        = string
}

variable "subnet_id" {
  description = "ID de la subred donde se desplegará la instancia"
  type        = string
}

variable "sg_id" {
  description = "ID del Security Group que se asociará a la instancia"
  type        = string
}

variable "instance_type" {
  description = "Tipo de instancia EC2"
  type        = string
  default     = "t3.micro"
}

variable "key_name" {
  description = "Nombre del key pair (opcional, no usado en este entorno)"
  type        = string
  default     = null
}

variable "tags" {
  description = "Etiquetas comunes aplicadas a los recursos"
  type        = map(string)
  default     = {}
}

variable "ecr_repository_url" {
  description = "URL del repositorio ECR desde donde se hará pull de la imagen"
  type        = string
  default     = null
}

variable "image_tag" {
  description = "Tag de la imagen a ejecutar"
  type        = string
  default     = "latest"
}