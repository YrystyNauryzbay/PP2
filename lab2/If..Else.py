#1
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#2
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#3  AND
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#4 OR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#5 to avoid getting an error
a = 33
b = 200

if b > a:
  pass