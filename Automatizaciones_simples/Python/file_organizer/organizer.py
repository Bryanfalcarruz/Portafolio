import os
import shutil

# Define file categories and their associated extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"]
}

def organize_folder(path):
    # Validate the input path
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return

    print(f"\nOrganizing folder: {path}")
    files = os.listdir(path)

    # Initialize statistics
    stats = {}
    total_processed = 0

    # Process each item in the folder
    for file in files:
        full_path = os.path.join(path, file)

        # Skip directories, process only files
        if os.path.isfile(full_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False

            # Check file extension and assign to a category
            for category, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    move_file(full_path, os.path.join(path, category))
                    stats[category] = stats.get(category, 0) + 1
                    total_processed += 1
                    moved = True
                    break

            # If no category matched, move to 'Others'
            if not moved:
                move_file(full_path, os.path.join(path, "Others"))
                stats["Others"] = stats.get("Others", 0) + 1
                total_processed += 1

    print("\nOrganization completed.")
    print("\nSummary:")
    print(f"Total files organized: {total_processed}")
    for category, count in stats.items():
        print(f"- {category}: {count}")

def move_file(file_path, target_folder):
    # Create the target folder if it does not exist
    os.makedirs(target_folder, exist_ok=True)

    # Build the destination path and move the file
    filename = os.path.basename(file_path)
    destination = os.path.join(target_folder, filename)
    shutil.move(file_path, destination)

    print(f"Moved: {filename} → {target_folder}")

# Prompt the user to enter a folder path
folder_path = input("Enter the full path of the folder to organize: ")
organize_folder(folder_path)