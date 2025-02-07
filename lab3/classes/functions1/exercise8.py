def order007(arr):
    result = []  
    for i in arr:
        if i == 0 or i == 7:
            result.append(i)  
    
#check
    if result[:3] == [0, 0, 7]:  
        print("True")
    else:
        print("False")


order007([1,2,4,0,0,5,7])  #  True
order007([1,0,2,4,0,5,7])  #  True
order007([1,7,2,0,4,5,0])  #  False
order007([0, 0, 7])        #  True
order007([0, 7, 0])        #  False
