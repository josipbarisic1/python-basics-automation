# FILE ORGANIZER
# Script that scans a folder
# and organizes files into subfolders by type

import os
import shutil

def sort_file(full_path_src, extension):
    match extension:
        case ".txt":
            full_path_dest = os.path.join("test_files", "text")
            if not os.path.exists(full_path_dest):
                os.makedirs(full_path_dest)
            shutil.move(full_path_src, full_path_dest)
        case ".png" | ".jpg" | ".jpeg" | ".webp":
            full_path_dest = os.path.join("test_files", "images")
            if not os.path.exists(full_path_dest):
                os.makedirs(full_path_dest)
            shutil.move(full_path_src, full_path_dest)
        case ".csv":
            full_path_dest = os.path.join("test_files", "csv")
            if not os.path.exists(full_path_dest):
                os.makedirs(full_path_dest)
            shutil.move(full_path_src, full_path_dest)

def sort_test_files():
    files = os.listdir("test_files/")
    files_moved = 0

    for file in files:
        full_path_src = os.path.join("test_files", file)
        is_file = os.path.isfile(full_path_src)
        if is_file:
            name, extension = os.path.splitext(file)
            extension = extension.lower()
            sort_file(full_path_src, extension)
            files_moved += 1
    
    print(f"\n[SUCCESS] Files organized successfully")
    print(f"  Files moved: {files_moved}")

if __name__ == "__main__":
    print("[INFO] Organizing files in test_files/...")
    sort_test_files()
