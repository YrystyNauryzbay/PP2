import re


with open(r'C:\Users\User\Desktop\PP2\LABs\lab5\row.txt', encoding="utf-8") as f:
        data = f.read()

print("Task 1")
matches = re.findall(r"a.*?b", data) 
print(matches if matches else "No matches found.")

print("Task 2")
matches = re.findall(r"ab{2,3}", data)
print(matches)

print('Task 3')
matches = re.findall(r"[a-z]+(?:_[a-z]+)*", data)
print(matches)

print('Task 4')
matches = re.findall(r"[A-Z][a-z]+", data)
print(matches)

print('Task 5')
matches = re.findall(r"a.*b", data)
print(matches)

print("Task 6")
matches=re.sub(r"[., ]",':',data)
print(matches)

print("Task 7")
matches=re.sub(r"_",'',data)
print(matches)

