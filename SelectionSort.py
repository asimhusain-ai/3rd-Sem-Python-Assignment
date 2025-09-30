def selectionsort(arr):
    n = len(arr)
    
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        
    return arr

print(selectionsort([8,2,9,4,1,8]))