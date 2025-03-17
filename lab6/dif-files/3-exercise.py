import os

def check_path(path):
    if os.path.exists(path):
        print("File Name:", os.path.basename(path))
        print("Directory Name:", os.path.dirname(path))
    else:
        print("Path does not exist")

path = r"/Users/bekzatshaiyrgozha/Documents/sample.txt"
check_path(path)
