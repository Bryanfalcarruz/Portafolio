========================================
## Organizador de Archivos - Proyecto DevOps
========================================

Automatización de organización de archivos con Python,
empaquetado en Docker y listo para futuros despliegues en la nube con prácticas DevOps.
Este proyecto comenzó como un script en Python para organizar archivos por tipo,
y fue evolucionado hacia un entorno DevOps completo con contenerización en Docker,
futuro despliegue en AWS e integración con CI/CD.

----------------------------------------
## Modo de uso (Python local)
----------------------------------------

Ejecutar en terminal:

python organizer.py --path RUTA [opciones]

Donde RUTA es la carpeta que se desea organizar.

----------------------------------------
## Opciones disponibles
----------------------------------------

--path RUTA
Ruta completa de la carpeta que se organizará. (Obligatorio)

--dry-run
Simula la organización sin mover archivos.
Útil para verificar qué pasaría antes de ejecutar realmente.

--exclude PATRONES
Patrones de archivos a excluir.
Ejemplo: --exclude *.tmp *.part
Si no se especifica, se aplican exclusiones por defecto:
*.tmp, *.part, *.crdownload, Thumbs.db, .DS_Store

--on-collision [skip | overwrite | rename]
Define qué hacer si un archivo con el mismo nombre ya existe en la carpeta destino.

    skip (por defecto): omite mover el archivo.
    overwrite: reemplaza el archivo existente.
    rename: crea un nuevo nombre único (ej: archivo (1).txt).

----------------------------------------
## Ejemplos
----------------------------------------

Organizar la carpeta Descargas:
python organizer.py --path "C:/Users/TuUsuario/Downloads"

Simular la organización sin mover nada:
python organizer.py --path "/home/usuario/Descargas" --dry-run

Excluir archivos temporales y de partes:
python organizer.py --path "/home/usuario/Descargas" --exclude *.tmp *.part

Sobrescribir archivos duplicados:
python organizer.py --path "C:/Users/TuUsuario/Downloads" --on-collision overwrite

Renombrar archivos duplicados en lugar de sobrescribirlos:
python organizer.py --path "/home/usuario/Descargas" --on-collision rename

----------------------------------------
## Uso con Docker
----------------------------------------

# Opción 1: Build local

Construir la imagen:
docker build -f docker/Dockerfile -t file-organizer .

Ejecutar en modo simulación:
docker run --rm -v "C:/Users/TuUsuario/Downloads:/data" file-organizer --path /data --dry-run

Ejecutar sobrescribiendo en colisión:
docker run --rm -v "C:/Users/TuUsuario/Downloads:/data" file-organizer --path /data --on-collision overwrite

# Opción 2: Usar imagen pública (Docker Hub)

Este proyecto está disponible en Docker Hub:
https://hub.docker.com/r/bryanf606/file-organizer

Descargar la imagen:
docker pull bryanf606/file-organizer:latest

Ejecutar en Windows:
docker run --rm -v "C:/Users/TuUsuario/Downloads:/data" bryanf606/file-organizer:latest --path /data --dry-run

Ejecutar en Linux/macOS:
docker run --rm -v "$HOME/Downloads:/data" bryanf606/file-organizer:latest --path /data --dry-run

Usar versión fija:
docker run --rm -v "$HOME/Downloads:/data" bryanf606/file-organizer:0.1.0 --path /data

----------------------------------------
## Roadmap
----------------------------------------

Etapas del proyecto:
1. Script en Python con CLI y opciones avanzadas. [X]
2. Contenerización con Docker.                    [X]
3. Infraestructura como Código con Terraform.     [ ] 
4. Despliegue en AWS (EC2 / Lambda / S3).         [ ]
5. Pipeline CI/CD con GitHub Actions.             [ ]

----------------------------------------
## Autor
----------------------------------------
Bryan Alcarruz  