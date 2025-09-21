import os
import shutil
import argparse
import fnmatch
from pathlib import Path

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"]
}

# Exclusiones por defecto
DEFAULT_EXCLUDES = ["*.tmp", "*.part", "*.crdownload", "Thumbs.db", ".DS_Store"]

def unique_dest(dest_dir: Path, filename: str) -> Path:
    """Genera un nombre único si el archivo ya existe (para on-collision=rename)."""
    base = Path(filename).stem
    ext = Path(filename).suffix
    cand = dest_dir / filename
    i = 1
    while cand.exists():
        cand = dest_dir / f"{base} ({i}){ext}"
        i += 1
    return cand

def move_file(file_path, target_folder, dry_run=False, on_collision="skip"):
    """Mueve un archivo respetando la política de colisión."""
    dest_dir = Path(target_folder)
    dest_dir.mkdir(parents=True, exist_ok=True)

    filename = os.path.basename(file_path)
    destination = dest_dir / filename

    if destination.exists():
        if on_collision == "skip":
            print(f"Skipped (exists): {filename} → {target_folder}")
            return
        elif on_collision == "rename":
            destination = unique_dest(dest_dir, filename)
            print(f"Renamed: {filename} → {destination.name}")
        elif on_collision == "overwrite":
            print(f"Overwriting: {filename}")

    if dry_run:
        print(f"Would move: {filename} → {destination}")
    else:
        shutil.move(file_path, destination)
        print(f"Moved: {filename} → {destination}")

def organize_folder(path: str, dry_run=False, exclude=None, on_collision="skip"):
    """Organiza los archivos de la carpeta según su extensión."""
    base = Path(path).expanduser().resolve()
    if not base.exists() or not base.is_dir():
        print(f"Path does not exist or is not a directory: {base}")
        return

    # Patrones de exclusión (si no se especifican, se usan los predeterminados)
    patterns = exclude if exclude else DEFAULT_EXCLUDES

    print(f"\nOrganizing folder: {base}")
    print(f"Excluding patterns: {patterns}")
    print(f"On collision policy: {on_collision}")
    files = os.listdir(base)

    stats = {}
    total_processed = 0

    for file in files:
        full_path = os.path.join(base, file)

        if os.path.isfile(full_path):
            # Verificar exclusiones
            if any(fnmatch.fnmatch(file, pattern) for pattern in patterns):
                print(f"Excluded: {file}")
                continue

            file_ext = os.path.splitext(file)[1].lower()
            moved = False

            for category, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    move_file(full_path, os.path.join(base, category), dry_run, on_collision)
                    stats[category] = stats.get(category, 0) + 1
                    total_processed += 1
                    moved = True
                    break

            if not moved:
                move_file(full_path, os.path.join(base, "Others"), dry_run, on_collision)
                stats["Others"] = stats.get("Others", 0) + 1
                total_processed += 1

    print("\nOrganization completed.")
    print("\nSummary:")
    print(f"Total files processed: {total_processed}")
    for category, count in stats.items():
        print(f"- {category}: {count}")

def parse_args():
    parser = argparse.ArgumentParser(
        description="Organize files in a folder by category (Images, Documents, etc.)."
    )
    parser.add_argument("--path", required=True, help="Full path of the folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Simulate actions without moving files")
    parser.add_argument(
        "--exclude",
        nargs="+",
        help="File patterns to exclude (e.g. *.tmp *.part). Defaults are used if not provided."
    )
    parser.add_argument(
        "--on-collision",
        choices=["skip", "overwrite", "rename"],
        default="skip",
        help="What to do if file exists: skip (default), overwrite, rename"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    organize_folder(args.path, dry_run=args.dry_run, exclude=args.exclude, on_collision=args.on_collision)

if __name__ == "__main__":
    main()