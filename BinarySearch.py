def binarysearch(nums, key):
    n = len(nums)
    start = 0
    end = n-1
    
    while start < end:
        mid = (start + end) // 2
        
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
        
    return None

result = binarysearch([1,2,3,4,5,67,8,9],4)

if result is None:
    print("Elememt Not Present")
else:
    print("Element Present at: ",result)