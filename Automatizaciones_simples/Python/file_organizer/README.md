========================================
## Organizador de Archivos - Instrucciones
========================================

Este script organiza los archivos de una carpeta según su extensión,
moviendo cada archivo a subcarpetas (Images, Documents, Videos, Music, Others).

----------------------------------------
## Modo de uso
----------------------------------------

Ejecuta en terminal:

    python organizer.py --path RUTA [opciones]

Donde RUTA es la carpeta que deseas organizar.

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
    - skip (por defecto): omite mover el archivo.
    - overwrite: reemplaza el archivo existente.
    - rename: crea un nuevo nombre único (archivo (1).txt, archivo (2).txt, etc.)

----------------------------------------
## Ejemplos
----------------------------------------

1. Organizar la carpeta Descargas:
    python organizer.py --path "C:/Users/TuUsuario/Downloads"

2. Simular la organización sin mover nada:
    python organizer.py --path "/home/usuario/Descargas" --dry-run

3. Excluir archivos temporales y de partes:
    python organizer.py --path "/home/usuario/Descargas" --exclude *.tmp *.part

4. Sobrescribir archivos duplicados:
    python organizer.py --path "C:/Users/TuUsuario/Downloads" --on-collision overwrite

5. Renombrar archivos duplicados en lugar de sobrescribirlos:
    python organizer.py --path "/home/usuario/Descargas" --on-collision rename

----------------------------------------
Resumen
----------------------------------------
- Clasifica los archivos en subcarpetas.
- Acepta exclusiones personalizadas.
- Permite simular antes de ejecutar.
- Maneja colisiones de nombre con 3 políticas distintas.

========================================
