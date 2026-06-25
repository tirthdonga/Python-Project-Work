def create_file():
    filename = input("Enter filename to create: ")
    with open(filename, 'w') as f:
        print(f"File {filename} created successfully.")

def write_file():
    filename = input("Enter filename: ")
    content = input("Enter content to write: ")
    with open(filename, 'w') as f:
        f.write(content)
    print("Content written successfully.")

def read_file():
    filename = input("Enter filename to read: ")
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File not found.")

def append_file():
    filename = input("Enter filename: ")
    content = input("Enter content to append: ")
    with open(filename, 'a') as f:
        f.write("\n" + content)
    print("Content appended successfully.")