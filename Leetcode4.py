nums = [2,2,2,3,4,4,4,5,5,7]
n = len(nums)
if n <= 2:
    print(n)
k = 1
for i in range(2, n):
    if nums[i] == nums[k-1]:
        k = k + 1
        nums[k] = nums[i]
print(k+1)