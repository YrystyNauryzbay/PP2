#1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#2

newlist = [x for x in range(10)]

print(newlist)

#3
newlist = [x for x in range(10) if x < 5]

print(newlist)