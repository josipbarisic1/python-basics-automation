# Day 3
# Script that reads a text file with names
# counts how many names exist
# and writes them in uppercase to a new file.

counter = 0

try:
    with open("names.txt", "r") as file_names, open("uppercase.txt", "w") as file_uppercase:
        for line in file_names:
            counter += 1
            file_uppercase.write(line.upper())
            
except FileNotFoundError:
    print("File doesn't exist")

print(f'Name count: {counter}')