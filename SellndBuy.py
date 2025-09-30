def maxProfit(nums):
    min_el = min(nums)
    max_el = max(nums)
    return max_el - min_el

print(maxProfit([8,2,1,6,7,3,2,9]))