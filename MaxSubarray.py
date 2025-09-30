def maxSubarray(nums):
    curr_sum = nums[0]
    max_sum = nums[0]
    
    for x in nums[1:]:
        curr_sum = max(curr_sum + x , x)
        max_sum = max(max_sum, curr_sum)
        
    return max_sum

print(maxSubarray([1,2,4,6,3,0]))