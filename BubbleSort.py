def bubblesort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubblesort([8,1,4,9,5,6]))