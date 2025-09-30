def sumofdigit(n):
    
    sum = 0
    
    for i in str(n):
        sum += int(i)
        
    return sum

print(sumofdigit(1625346))