Este archivo está disponible en español e inglés.  
This file is available in Spanish and English.

---

# Organizador de Archivos (File Organizer)

Script de automatización en Python que organiza archivos en una carpeta según su tipo, moviéndolos a subcarpetas específicas. Es multiplataforma (Windows, Linux, macOS) y no requiere dependencias externas.

---

## ¿Qué hace?

- Analiza los archivos de una carpeta especificada por el usuario.
- Detecta su extensión y los clasifica como:
  - Imágenes, Documentos, Videos, Música u Otros.
- Crea carpetas si no existen.
- Mueve cada archivo a la carpeta correspondiente.
- Muestra un resumen al finalizar.

---

## Cómo se usa

1. Ejecutar el script:
   ```bash
   python organizer.py
Ingresar la ruta completa de la carpeta que deseas organizar.

Ejemplos:

En Windows:
C:/Users/TuUsuario/Downloads

En Linux o macOS:
/home/usuario/Descargas

## Estructura generada
nginx
Copiar código
Carpeta original/
├── Images/
├── Documents/
├── Videos/
├── Music/
└── Others/

Tecnologías utilizadas
Python3

Módulos estándar: os, shutil

## Posibles usos
-Ordenar automáticamente carpetas de descargas.
-Clasificar archivos en pendrives o carpetas compartidas.
-Automatizar la limpieza de archivos en equipos personales o de oficina.

----------------------------------------------------------------------------------------

## File Organizer
Python automation script that organizes files in a folder by type, moving them into specific subfolders. It is cross-platform (Windows, Linux, macOS) and requires no external dependencies.

## What it does
Scans the files in a folder specified by the user.

Detects their extensions and classifies them as:

Images, Documents, Videos, Music, or Others.

Creates folders if they do not exist.

Moves each file to the appropriate folder.

Displays a summary when finished.

## How to use
Run the script: 
python organizer.py

Enter the full path of the folder you want to organize.

## Examples:

On Windows: C:/Users/YourUser/Downloads
On Linux or macOS: /home/youruser/Downloads

## Generated structure

Original folder/
├── Images/
├── Documents/
├── Videos/
├── Music/
└── Others/

Technologies used
Python 3

Standard modules: os, shutil

## Possible use cases

Automatically organize download folders.

Classify files on USB drives or shared folders.

Automate file cleanup on personal or work computers.