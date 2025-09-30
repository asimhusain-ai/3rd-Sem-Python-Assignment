def TwoSum(nums, target):
    dick = {}
    for i , num in enumerate(nums):
        rem = target - num
        if rem in dick:
            return [dick[rem], i]
        dick[num]= i
        
print(TwoSum([1,3,7,6,9,3,1], 15))