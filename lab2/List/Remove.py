#1
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#If there are more than one item with the specified value, 
# the remove() method removes the first occurrence:

#2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#3
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#If you do not specify the index, the pop() method removes the last item

#4
thislist = ["apple", "banana", "cherry"]
del thislist
#or you can use clear()
