def fact(num):
    if num < 1:
        return 1
    else:
        return num * fact(num - 1)
    
s1 = fact(10)
print(s1)