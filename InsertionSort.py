def insertionsort(nums):
    n = len(nums)
    
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
            
        nums[j+1] =  key
    return nums

s1 = insertionsort([9,6,1,4,8,5])
print(s1)