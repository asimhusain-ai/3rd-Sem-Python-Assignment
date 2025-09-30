def fr(nums):
    freq = {}
    
    for ch in nums:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
            
    return max(freq, key=freq.get)
print(fr([2,3,3,4,4,5,5,5,5,5]))