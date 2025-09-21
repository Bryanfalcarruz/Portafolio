# Organizador de Archivos (File Organizer)

Script de automatización en Python que organiza archivos en una carpeta según su tipo, moviéndolos a subcarpetas específicas.  
Es multiplataforma (Windows, Linux, macOS) y no requiere dependencias externas.

---

## Función

- Analiza los archivos de una carpeta especificada por el usuario mediante el parámetro `--path`.
- Detecta su extensión y los clasifica como:
  - Imágenes, Documentos, Videos, Música u Otros.
- Crea carpetas si no existen.
- Mueve cada archivo a la carpeta correspondiente.
- Permite ejecutar en **modo simulación** con `--dry-run`, mostrando lo que haría sin mover nada.
- Permite **excluir archivos** por patrón con `--exclude` (ejemplo: `*.tmp *.part`).
  - Si no se especifica, aplica exclusiones por defecto: `*.tmp`, `*.part`, `*.crdownload`, `Thumbs.db`, `.DS_Store`.
- Muestra un resumen al finalizar.

---

## Cómo se usa


Ejecutar el script en terminal:

python organizer.py --path "RUTA/DE/TU/CARPETA"

## Ejemplos

En Windows:
python organizer.py --path "C:\Users\TuUsuario\Downloads"

En Linux o macOS:
python organizer.py --path "/home/usuario/Descargas"

## Opciones adicionales

Simulación (dry run):
python organizer.py --path "C:\Users\TuUsuario\Downloads" --dry-run

Excluir archivos por patrón:
python organizer.py --path "C:\Users\TuUsuario\Downloads" --exclude *.bak *.old

Manejo de duplicados (--on-collision)
Define qué hacer si el archivo ya existe en la carpeta de destino:
  -skip (por defecto): no mueve si existe.
  -rename: crea un nombre único con sufijo (1), (2), etc.
  -overwrite: reemplaza el archivo existente.

# Renombrar duplicados
python organizer.py --path "RUTA/DE/TU/CARPETA" --on-collision rename

# Sobrescribir duplicados
python organizer.py --path "RUTA/DE/TU/CARPETA" --on-collision overwrite

## Estructura generada
Carpeta original/
├── Images/
├── Documents/
├── Videos/
├── Music/
└── Others/

Python 3
Módulos estándar: os, shutil, argparse, pathlib, fnmatch

## Posibles usos
Ordenar automáticamente carpetas de descargas.
Clasificar archivos en pendrives o carpetas compartidas.
Automatizar la limpieza de archivos en equipos personales o de oficina.