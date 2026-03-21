# Day 8
# Script that scans a folder
# renames files based on rules
# and organizes them into subfolders.

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

    for file in files:
        full_path_src = os.path.join("test_files", file)
        is_file = os.path.isfile(full_path_src)
        if is_file:
            name, extension = os.path.splitext(file)
            extension = extension.lower()
            sort_file(full_path_src, extension)

if __name__ == "__main__":
    sort_test_files()
            


                




