def missing_num(nums):
    n = len(nums)
    
    for i in range(0, n+1):
        if i not in nums:
            return i 
        
s1 = missing_num([0,1,2,3,4,5,7,8,9])
print(s1)