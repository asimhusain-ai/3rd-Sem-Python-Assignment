matt = [[2,4,7],[9,5,1],[3,7,4]]

rows = len(matt)
cols = len(matt[0])

for i in range(rows):
    for j in range(cols):
        if j >= i:
            print(matt[i][j],end="     ")
        else:
            print("*",end="     ")
    print()
    print()