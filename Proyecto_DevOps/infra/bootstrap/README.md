========================================
# Infraestructura con Terraform
========================================

Esta carpeta contiene la definición de la infraestructura necesaria para el despliegue del proyecto.
Actualmente está configurado un backend remoto en AWS para almacenar el estado de Terraform de forma segura y compartida.

## Backend remoto (Terraform state)

S3 bucket: tfstate-file-organizer-bs79xp
DynamoDB table: tf-lock-file-organizer
Región: us-west-2
Archivo de configuración: backend.hcl

## Propósito
   Mantener el estado de Terraform en un lugar centralizado (S3).
   Proteger contra modificaciones concurrentes mediante locking en DynamoDB.
   Añadir seguridad con versionado, cifrado AES256 y bloqueo de acceso público.

## Flujo de trabajo

Inicializar Terraform con el backend remoto:

   terraform init -backend-config="backend.hcl"

Validar y aplicar cambios en el entorno dev:

   terraform validate
   terraform plan -var-file=env/dev.tfvars
   terraform apply -var-file=env/dev.tfvars

## Prácticas aplicadas

.terraform/ y *.tfstate están en .gitignore.
S3 con versionado y cifrado AES256.
DynamoDB con billing PAY_PER_REQUEST (sin costos fijos).
Tags de proyecto aplicados a los recursos.