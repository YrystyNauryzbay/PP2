from itertools import permutations

def print_permutations(s):
    perm_list = permutations(s) 
    for perm in perm_list:
        print(''.join(perm)) 

user_input = input("Enter: ")
print_permutations(user_input)
