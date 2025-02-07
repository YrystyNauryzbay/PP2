def unique(mylist):
    result = []
    for i in mylist:
        if i not in result: 
            result.append(i)
    return result

n = int(input("n: "))
mylist = []
for i in range(n):
    number = int(input("number: "))
    mylist.append(number)
print(unique(mylist))