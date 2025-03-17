size_list = input("Enter space-separated numbers: ")
my_list = list(map(int, size_list.split()))

multiply = 1
for i in my_list:
    multiply *= i

print("Product of all numbers:", multiply)
