import os

def list_contents(path):
    if not os.path.exists(path):
        print("Path does not exist.")
        return

    print("Directories:")
    print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

    print("Files:")
    print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

    print("All contents:")
    print(os.listdir(path))

path = r"/Users/bekzatshaiyrgozha/Documents"
list_contents(path)
