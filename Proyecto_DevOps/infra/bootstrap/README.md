# Terraform Bootstrap – Remote Backend
Este módulo crea los recursos necesarios para usar Terraform con un estado remoto en AWS:

- **S3 Bucket** para almacenar el state (con versionado y cifrado).  
- **DynamoDB Table** para bloqueo del estado (locking).  

## Uso rápido
1. Ir al directorio `bootstrap`.
2. Ejecutar:
   terraform init
   terraform apply
3. Guardar los outputs (`tfstate_bucket_name`, `lock_table_name`) y usarlos en `infra/backend.hcl`.

Este paso se hace solo una vez para preparar el backend remoto de Terraform.
