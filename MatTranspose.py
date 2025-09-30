matt = [[2,4,8],[-9,4,1]]

rows = len(matt)
cols = len(matt[0])

result = [[0] * rows for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        print(matt[i][j],end="  ")
        result[j][i] = matt[i][j]
    
print(result,end="  ")