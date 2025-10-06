variable "project_name" {
  description = "Prefijo para nombrar el repositorio ECR"
  type        = string
}

variable "image_mutability" {
  description = "Inmutabilidad de tags en ECR: MUTABLE o IMMUTABLE"
  type        = string
  default     = "IMMUTABLE"
}

variable "scan_on_push" {
  description = "Habilita análisis de vulnerabilidades al hacer push"
  type        = bool
  default     = true
}

variable "encryption_type" {
  description = "Cifrado del repositorio (KMS o AES256)"
  type        = string
  default     = "AES256"
}

variable "kms_key_arn" {
  description = "ARN de clave KMS si encryption_type = KMS"
  type        = string
  default     = null
}

variable "tags" {
  description = "Etiquetas comunes"
  type        = map(string)
  default     = {}
}