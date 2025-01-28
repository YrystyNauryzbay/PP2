#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) #result:apple

#3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) #result:apple cherry

#4
fruits = ["apple", "banana", "cherry", "mango"]
for x in fruits[:3]:
  print(x)

#5
for x in [0, 1, 2]:
  pass