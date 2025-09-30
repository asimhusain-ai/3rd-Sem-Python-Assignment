def evenodd(nums):
    sumeven = []
    sumodd = []
    for i in nums:
        if i % 2 == 0:
            sumeven.append(i)
        else:
            sumodd.append(i)
    return sumeven , sumodd
print(evenodd([4,5,6,7,8]))