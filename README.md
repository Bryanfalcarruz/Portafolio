=========================================
Portafolio de proyectos personales y técnicos.
=========================================

Incluye scripts, automatizaciones, ejercicios lógicos y desarrollos prácticos.  


--------------------------------------------------
## Proyecto en curso: **DevOps – File Organizer**
--------------------------------------------------

Proyecto orientado a DevOps basado en un organizador de archivos en Python.
La aplicación fue contenerizada con Docker y actualmente se encuentra en proceso de despliegue en AWS mediante Terraform, aplicando buenas prácticas de Infraestructura como Código (IaC), modularización y documentación profesional.

-----------------------------------------
## Estado actual (05-10-2025)
-----------------------------------------

  -Implementado el módulo ECR (Elastic Container Registry) para almacenar imágenes Docker privadas.
  -Repositorio file-organizer-repo creado con:
    -Cifrado AES-256.
    -Etiquetas inmutables (IMMUTABLE).
    -Análisis de vulnerabilidades habilitado (scan_on_push = true).
  -Integración del módulo compute con ECR, permitiendo a la instancia EC2 hacer docker pull automáticamente (pendiente de subir la imagen).
  -Actualización del bloque user_data para ejecución automática del contenedor. 
  -Instancia EC2 validada con Docker y SSM en ejecución (systemctl status).
  -Capturas y documentación añadidas en docs/screenshots/ecr/ y docs/screenshots/compute/.

-----------------------------------------
## Próximos pasos
-----------------------------------------

  -Subir la imagen Docker del File Organizer a ECR (docker push).
  -Verificar la ejecución automática del contenedor en EC2 (docker ps).
  -Implementar observabilidad básica con CloudWatch Logs y métricas.
  -Completar los README de infra/ y modules/ecr.
  -Crear un video corto de demostración mostrando el flujo Terraform → AWS → Docker.

-----------------------------------------
## Actualización anterior (24-09-2025)
-----------------------------------------

  -Avances incorporados en esa fecha
  -Infraestructura base creada con Terraform (modular y documentada).
  -Implementación del bootstrap (S3 + DynamoDB) como backend remoto para el estado de Terraform.
  -Módulo network desplegado correctamente:
    -VPC, subred pública, Internet Gateway, Route Table y Security Group base.
  -Módulo compute creado y validado:
    -Instancia EC2 t3.micro (Amazon Linux 2).
    -Instalación automática de Docker.
    -Acceso seguro por Session Manager (sin puertos SSH expuestos).
  -Validaciones exitosas con terraform plan y terraform validate.
  -Evidencias añadidas en docs/screenshots/network/ y docs/screenshots/compute/.

-----------------------------------------
## Estructura del repositorio
-----------------------------------------

- Algoritmos_y_scripts/ → Scripts en Python y ejercicios de práctica.  
- AWS/ → Prácticas y ejemplos con servicios AWS (CloudFormation, RDS, VPC).  
- Proyecto_DevOps/ → Proyecto principal DevOps (Docker + Terraform + AWS).  

---

*Este README se actualiza de forma continua para reflejar el progreso del proyecto.*  