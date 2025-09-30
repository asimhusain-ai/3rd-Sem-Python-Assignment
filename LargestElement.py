# Using Built in function

def largest(num):
    return max(num)
print(largest([3,5,8,1,9,6,4]))

# Using Iterative Approach

def large(nums):
    mx = nums[0]
    
    for i in nums:
        if i > mx:
            mx = i
            
    return mx
print(large([6,8,3,2,11,6,7]))