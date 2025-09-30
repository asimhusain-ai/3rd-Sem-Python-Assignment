for i in range(5, 0, -1):
    for j in range(1, 6 - i):
        print(" ",end=" ")
    for k in range(1,i+1):
        if i == 5 or k == 1 or k == i:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()