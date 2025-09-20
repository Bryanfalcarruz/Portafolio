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

def organize_folder(path: str):
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
                    move_file(full_path, os.path.join(base, category))
                    stats[category] = stats.get(category, 0) + 1
                    total_processed += 1
                    moved = True
                    break

            if not moved:
                move_file(full_path, os.path.join(base, "Others"))
                stats["Others"] = stats.get("Others", 0) + 1
                total_processed += 1

    print("\nOrganization completed.")
    print("\nSummary:")
    print(f"Total files organized: {total_processed}")
    for category, count in stats.items():
        print(f"- {category}: {count}")

def move_file(file_path, target_folder):
    os.makedirs(target_folder, exist_ok=True)
    filename = os.path.basename(file_path)
    destination = os.path.join(target_folder, filename)
    shutil.move(file_path, destination)
    print(f"Moved: {filename} → {target_folder}")

def parse_args():
    parser = argparse.ArgumentParser(
        description="Organize files in a folder by category (Images, Documents, etc.)."
    )
    parser.add_argument("--path", required=True, help="Full path of the folder to organize")
    return parser.parse_args()

def main():
    args = parse_args()
    organize_folder(args.path)

if __name__ == "__main__":
    main()