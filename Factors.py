def factorsofnum(nums):
    result = []
    
    for i in range(1,nums+1):
        if nums % i == 0:
            result.append(i)
    return result

print(factorsofnum(20))