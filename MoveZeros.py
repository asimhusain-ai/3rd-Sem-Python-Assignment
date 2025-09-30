def movezeros(nums):
    i = 0
    j = 0
    
    while i < len(nums):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        i += 1
    return nums

print(movezeros([1,2,3,4,5,6,0,0,0,0,0,2,4,5]))