nums = [2,3,5,7,9]

ans = []
ans.append(nums[0])

for i in range(1, len(nums)):
    x = ans[i-1]  + nums[i]
    ans.append(x)
print(ans)