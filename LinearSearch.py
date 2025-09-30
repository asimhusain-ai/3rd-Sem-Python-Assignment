def linearsearch(nums, key):
    n = len(nums)
    for i in range(0, n):
        if nums[i] == key:
            return i
    return None

result = linearsearch([1,2,4,6,9,7,8], 6)
if result is None:
    print("Not Present")
    
else:
    print("Element Present at", result)