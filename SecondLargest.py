# def secondlargest(nums):
#     nums = list(set(nums))
#     nums = sorted(nums)
#     return nums[-2]

# print(secondlargest([3,6,9,8,7,6,8,9]))

# Another Approach

def secondlargest(nums):
    largest = float("-inf")
    second_largest = float("-inf")
    
    for i in range(len(nums)):
        largest = max(nums)
        
    for x in range(len(nums)):
        if nums[x] > second_largest and nums[x] != largest:
            second_largest = nums[x]
            
    return second_largest

print(secondlargest([5,6,9,3,1,4]))