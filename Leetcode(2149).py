def rearrange(nums):
    pos = [x for x in nums if x >= 0]
    neg = [x for x in nums if x < 0]
    
    result = []
    i = 0
    j = 0
    
    while i<len(pos) and j<len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1
        
    return result

s1 = rearrange([2,-1,5,6,7,-3,-9,-7])
print(s1)