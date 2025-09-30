# def rotarr(nums):
#     n = len(nums)
    
#     nums[:] = nums[1:n] + [nums[0]]
#     return nums

# print(rotarr([2,3,4,5,6,9,7]))

def rotarr(nums):
    for i in range(0,1):
        ele = nums.pop()
        nums.insert(0,ele)
        
    return nums

s1=rotarr([1,2,3,4,5,6,7])
print(s1)