def has_33(num):
    n = 0
    for i in num:
        if(i == 3):
            n+=1
        else:
            n=0
        if(n>=2):
            return True
    return False
print(has_33([1, 3, 3]))    
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3])) 