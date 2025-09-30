# Method 1

# def rotatekelement(nums, k):
#     n = len(nums)
    
#     if nums ==0 and k == 0:
#         return nums
    
#     k = k % n
    
#     nums[:] = nums[-k:] + nums[:-k]
#     return nums
# s1 = rotatekelement([1,2,3,4,5,6,7,8,9], 6)
# print(s1)

# Method 2

def rotatekelements(nums, k):
    for i in range(0,k):
        ele = nums.pop()
        nums.insert(0,ele)
        
    return nums
s1 = rotatekelements([1,2,3,4,5,6,7,8,9], 5)
print(s1)