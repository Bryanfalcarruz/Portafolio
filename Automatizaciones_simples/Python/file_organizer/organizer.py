import os
import shutil
import argparse
from pathlib import Path

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"]
}

def organize_folder(path: str, dry_run: bool = False):
    base = Path(path).expanduser().resolve()
    if not base.exists() or not base.is_dir():
        print(f"Path does not exist or is not a directory: {base}")
        return

    print(f"\nOrganizing folder: {base}")
    files = os.listdir(base)

    stats = {}
    total_processed = 0

    for file in files:
        full_path = os.path.join(base, file)

        if os.path.isfile(full_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False

            for category, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    move_file(full_path, os.path.join(base, category), dry_run)
                    stats[category] = stats.get(category, 0) + 1
                    total_processed += 1
                    moved = True
                    break

            if not moved:
                move_file(full_path, os.path.join(base, "Others"), dry_run)
                stats["Others"] = stats.get("Others", 0) + 1
                total_processed += 1

    print("\nOrganization completed.")
    print(f"Total files organized: {total_processed}")
    for category, count in stats.items():
        print(f"- {category}: {count}")

def move_file(file_path, target_folder, dry_run: bool = False):
    os.makedirs(target_folder, exist_ok=True)
    filename = os.path.basename(file_path)
    destination = os.path.join(target_folder, filename)

    if dry_run:
        print(f"Would move: {filename} → {target_folder}")
    else:
        shutil.move(file_path, destination)
        print(f"Moved: {filename} → {target_folder}")

def parse_args():
    parser = argparse.ArgumentParser(description="Organize files by type")
    parser.add_argument("--path", required=True, help="Full path of the folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without moving files")
    return parser.parse_args()

def main():
    args = parse_args()
    organize_folder(args.path, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
