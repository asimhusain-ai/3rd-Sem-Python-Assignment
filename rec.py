def checkarr(nums):
    n = len(nums)
    
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            return False
        return True

print(checkarr([1,2,3,4,5,7,6,8,9]))