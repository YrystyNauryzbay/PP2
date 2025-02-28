import re

print("Task 8")
data = 'ThisIsAStringWithUppercaseLetters'
print(re.findall(r"[A-Z][^A-Z]*", data))

print("Task 9")
data = 'ThisIsAStringWithUppercaseLetters'
m = re.sub(r'([a-z])([A-Z])', r'\1 \2', data)
print(m)

print("Task 10")
data = 'ThisIsAStringWithUppercaseLetters'
matches=re.sub(r"[A-Z]",'_',data)
print(matches)