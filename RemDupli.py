# def remdup(nums):
#     return list(set(nums))

# print(remdup([1,2,2,3,4,4,4,5,6,7,7]))


def remdupli(nums):
    n = len(nums)
    freq = {}
    for ch in nums:
        if ch not in freq:
            freq[ch] = 1
    return list(freq)


print(remdupli([2,2,3,4,5,5,6,7]))