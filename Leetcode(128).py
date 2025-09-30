def LongestSubsequence(nums):
    nums = set(nums)
    count = 0
    
    for x in nums:
        if x - 1 not in nums:
            seq = 1
            while x + seq in nums:
                seq += 1
            count = max(count, seq)
    return count

s1 = LongestSubsequence([3,6,2,1,4,9,5])
print(s1)