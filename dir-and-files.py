# 1
import os

def list_contents(path="."):
    items = os.listdir(path)
    dirs = [i for i in items if os.path.isdir(os.path.join(path, i))]
    files = [i for i in items if os.path.isfile(os.path.join(path, i))]

    
    for d in dirs:
        print(f"  - {d}")

    
    for f in files:
        print(f"  - {f}")

    
    for i in items:
        print(f"  - {i}")

list_contents()


# 2
import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)

    print(f"Жол: {path}")
    print(f"Бар ма: {'Иә' if exists else 'Жоқ'}")
    print(f"Оқуға болады ма: {'Иә' if readable else 'Жоқ'}")
    print(f"Жазуға болады ма: {'Иә' if writable else 'Жоқ'}")
    print(f"Орындауға болады ма: {'Иә' if executable else 'Жоқ'}")

check_access("test.txt")


# 3
import os

def check_path(path):
    if os.path.exists(path):
        print(f"Жол бар: {path}")
        print(f"Каталог: {os.path.dirname(path)}")
        print(f"Файл атауы: {os.path.basename(path)}")
    else:
        print("Жол жоқ")

check_path("test.txt")



# 4
def count_lines(file):
    try:
        with open(file, "r") as f:
            print(f"Жол саны: {sum(1 for _ in f)}")
    except FileNotFoundError:
        print("Файл табылмады")

count_lines("test.txt")

# 5
def write_list_to_file(file, data):
    try:
        with open(file, "w") as f:
            f.writelines("\n".join(data))
        print("Тізім файлға жазылды")
    except Exception as e:
        print(f"Қате: {e}")

write_list_to_file("test.txt", ["Алма", "Алмұрт", "Жүзім"])


# 6
import string

def create_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", "w") as f:
            f.write(f"Бұл {letter}.txt файлы\n")
    print("Файлдар жасалды")

create_files()

# 7
def copy_file(source, destination):
    try:
        with open(source, "r") as src, open(destination, "w") as dst:
            dst.write(src.read())
        print("Файл көшірілді")
    except FileNotFoundError:
        print("Бастапқы файл табылмады")

copy_file("source.txt", "destination.txt")


# 8
import os

def delete_file(file):
    if os.path.exists(file):
        os.remove(file)
        print("Файл жойылды")
    else:
        print("Файл табылмады")

delete_file("test.txt")

