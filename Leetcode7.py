matrix = [[1,3,5,8,3],[3,2,5,8,1],[1,5,9,2,3],[9,8,6,3,2]]

m = len(matrix)
n = len(matrix[0])

mat = []
count = 0
tot = m * n

rowstart = 0
colstart = 0
rowend = m - 1
colend = n - 1

while count < tot:
    
    for i in range(colstart , colend + 1):
        mat.append(matrix[rowstart][i])
        count += 1
    rowstart += 1
    if count == tot:
        break
    
    for i in range(rowstart, rowend + 1):
        mat.append(matrix[i][colend])
        count += 1
    colend -= 1
    if count ==  tot:
        break
    
    for i in range(colend, colstart - 1,-1):
        mat.append(matrix[rowend][i])
        count += 1
    rowend -= 1
    if count == tot:
        break
    
    for i in range(rowend, rowstart -1, -1):
        mat.append(matrix[i][colstart])
        count += 1
    colstart += 1
    if count == tot:
        break
print(mat)