=========================================
Módulo compute
=========================================

Este módulo crea la capa de cómputo principal del proyecto File Organizer, desplegando una instancia EC2 con Docker habilitado y acceso administrativo mediante AWS Systems Manager (SSM).

-----------------------------------------
## Objetivo
-----------------------------------------

Proporcionar una instancia liviana y segura para ejecutar el contenedor del File Organizer sin necesidad de acceso SSH, utilizando infraestructura totalmente definida como código (IaC).

-----------------------------------------
## Recursos creados
-----------------------------------------

Instancia EC2
    Tipo: t3.micro
    Sistema operativo: Amazon Linux 2
    Subred: file-organizer-public-a (zona us-west-2a)
    Asignación automática de IP pública habilitada
    Script user_data que instala y habilita Docker
Rol e Instance Profile
    Rol IAM con permisos:
        AmazonSSMManagedInstanceCore (para conexión por SSM)
        AmazonS3ReadOnlyAccess (para acceso a bucket de estado o archivos del proyecto)
Configuración de red
    Security Group base heredado del módulo network
    Sin puertos de entrada abiertos (todo ingress bloqueado)
    Tráfico saliente (egress) completamente permitido

-----------------------------------------
## Variables de entrada
-----------------------------------------

project_name: Nombre del proyecto utilizado para el etiquetado y la nomenclatura de los recursos creados.
subnet_id: Identificador de la subred donde se desplegará la instancia EC2.
sg_id: Identificador del Security Group asociado a la instancia, heredado del módulo network.
instance_type: Tipo de instancia EC2 a utilizar. Por defecto se define t3.micro.
tags: Conjunto de etiquetas comunes aplicadas a todos los recursos del módulo.

-----------------------------------------
## Outputs generados
-----------------------------------------

instance_id: ID único de la instancia EC2 creada por el módulo.
public_ip: Dirección IP pública asignada automáticamente a la instancia al momento del despliegue.
iam_role_name: Nombre del rol IAM asociado a la instancia, el cual otorga permisos de SSM y acceso de solo lectura a S3.

-----------------------------------------
## Arquitectura
-----------------------------------------

El módulo compute se integra con la red creada previamente:
la instancia se lanza dentro de la VPC y subred pública del módulo network, utilizando el Security Group base.
El acceso administrativo se realiza únicamente mediante AWS Systems Manager (SSM), eliminando la necesidad de llaves SSH.

-----------------------------------------   
## Evidencias
-----------------------------------------

Las capturas del despliegue se almacenan en:

docs/screenshots/