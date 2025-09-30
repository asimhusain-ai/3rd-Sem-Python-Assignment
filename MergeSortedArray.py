def mergeSortedarray(num1, num2):
    
    merge = sorted(set(num1+num2))
    
    return merge

s1 = mergeSortedarray([1,2,3,4,5,8,9], [2,3,4,6,7,8])
print(s1)