def armstrong(n):
    power = len(str(n))
    sum = 0
    
    for i in str(n):
        sum += int(i) ** power
        
    if n == sum:
        return "Arm"
    else:
        return "Not Arm"
    
print(armstrong(1634))