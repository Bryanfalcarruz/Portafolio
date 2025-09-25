Portafolio de proyectos personales y técnicos. Incluye scripts, automatizaciones, ejercicios lógicos y desarrollos prácticos.  

---

## Proyecto en curso: **DevOps – File Organizer**
Actualmente estoy desarrollando un proyecto orientado a DevOps, tomando como base un organizador de archivos en Python que fue contenerizado con Docker y que ahora está siendo desplegado en AWS con Terraform.

## Estado actual (24-09-2025)
- ✅ Script en Python listo (CLI con opciones `--dry-run`, `--exclude`, `--on-collision`).  
- ✅ Contenerización con Docker (`Dockerfile` y `.dockerignore`).  
- ✅ Buenas prácticas Git (ramas por feature, PR y merges).  
- ✅ Documentación inicial en `docs/`.  
- **Etapa actual**: Creando infraestructura en AWS con Terraform.  
  - Implementando bootstrap (S3 + DynamoDB) para backend remoto de Terraform.  
  - Preparando entorno de red mínima (VPC + subredes + SGs).  

### Próximos pasos
- Configurar almacenamiento en S3 para el flujo del organizador (input/output).  
- Desplegar el contenedor en EC2/ECS.  
- Integrar CI/CD (GitHub Actions).  
- Añadir observabilidad (CloudWatch logs/metrics).  

---

## Estructura del repositorio
- Algoritmos_y_scripts/ → Scripts en Python y ejercicios de práctica.  
- AWS/ → Prácticas y ejemplos con servicios AWS (CloudFormation, RDS, VPC).  
- Proyecto_DevOps/ → Proyecto principal DevOps (Docker + Terraform + AWS).  

---

*Este README se actualiza de forma continua para reflejar el progreso del proyecto.*  