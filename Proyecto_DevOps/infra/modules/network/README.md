======================================== 
## Módulo network 
======================================== 

Este módulo define la infraestructura de red base del proyecto File Organizer, encargada de proporcionar conectividad segura y controlada dentro del entorno AWS. ---------------------------------------- 
## Objetivo 
---------------------------------------- 
Establecer una red simple y funcional para las instancias del entorno dev, con salida controlada a internet y sin puertos expuestos públicamente. ---------------------------------------- 
## Recursos creados 
---------------------------------------- 
VPC: 
    Nombre: file-organizer-vpc 
    CIDR: 10.0.0.0/16 
    DNS support y hostnames habilitados. 
Subred pública: 
    Nombre: file-organizer-public-a 
    CIDR: 10.0.1.0/24 
    Zona de disponibilidad: us-west-2a 
    Asignación automática de IP pública al lanzar instancias. 
Internet Gateway: 
Nombre: file-organizer-igw 
    Proporciona conectividad externa a la subred pública. 
Route Table pública: 
    Nombre: file-organizer-rt-public 
    Ruta principal: 0.0.0.0/0 → IGW 
    Asociada directamente a la subred pública. 
Security Group base: 
    Nombre: file-organizer-sg-base 
    Sin reglas de entrada (ingress). 
    Todo el tráfico de salida permitido (egress 0.0.0.0/0). 
Variables de entrada 
    project_name: nombre del proyecto para etiquetado y nombres de recursos. 
    vpc_cidr: rango CIDR utilizado por la VPC. 
    public_subnet_cidr: rango CIDR utilizado por la subred pública. 
    tags: conjunto de etiquetas aplicadas a todos los recursos. 
Outputs generados 
    vpc_id: identificador de la VPC creada. 
    public_subnet_id: identificador de la subred pública. 
    sg_base_id: identificador del Security Group base. 

---------------------------------------- 
## Arquitectura 
---------------------------------------- 
La red se compone de una VPC principal con una única subred pública conectada a un Internet Gateway. Esta configuración permite desplegar instancias con acceso a internet sin exponer puertos, utilizando AWS Systems Manager (SSM) para el acceso administrativo. 

## Evidencias 
----------------------------------------
Las capturas del despliegue se almacenan en: docs/screenshots/