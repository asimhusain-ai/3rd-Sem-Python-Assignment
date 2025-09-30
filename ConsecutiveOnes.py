def consecutiveones(nums):
    count = mx = 0
    if not nums:
        return 0
    
    for i in nums:
        if i == 1:
            count += 1
            mx = max(mx, count)
        else:
            count = 0
            
    return mx

print(consecutiveones([1,2,1,1,1,3,4,0,0,7,5,1,1,1,1,1]))