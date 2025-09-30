for i in range(1,6):
    for j in range(1,6 - i):
        print(" ", end=" ")
    for k in range(1, i * 2):
        if k == 1 or i == 5 or k == 2 * i - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

