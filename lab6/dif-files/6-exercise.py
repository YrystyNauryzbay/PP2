import string
import os

output_folder = r"C:\Users\User\Desktop\PP2\LABs\lab6\dif-files"
os.makedirs(output_folder, exist_ok=True)

def generate_files():
    for letter in string.ascii_uppercase:
        filename = os.path.join(output_folder, f"{letter}.txt")
        with open(filename, 'w') as f:
            f.write(f"This is file {letter}.txt")
        print(f"Created: {filename}")

generate_files()
