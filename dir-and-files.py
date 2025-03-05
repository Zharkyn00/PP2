import os
import shutil

# 1
def task1(path):
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

# 2
def task2(path):
    return os.path.exists(path), os.access(path, os.R_OK), os.access(path, os.W_OK), os.access(path, os.X_OK)

# 3
def task3(path):
    if os.path.exists(path):
        return os.path.basename(path), os.path.dirname(path)
    return None

# 4
def task4(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return sum(1 for _ in file)

# 5
def task5(file_path, lst):
    with open(file_path, "w", encoding="utf-8") as file:
        for item in lst:
            file.write(str(item) + "\n")

# 6
def task6(directory):
    os.makedirs(directory, exist_ok=True)
    for letter in range(ord('A'), ord('Z') + 1):
        with open(os.path.join(directory, f"{chr(letter)}.txt"), "w") as f:
            f.write(f"{chr(letter)} file\n")

# 7
def task7(source, destination):
    shutil.copyfile(source, destination)

# 8
def task8(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        return True
    return False
