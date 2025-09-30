def matzeros(matt):
    rows , cols = len(matt), len(matt[0])
    rowzero = []
    colzero = []
    
    for i in range(rows):
        for j in range(cols):
            if matt[i][j] == 0:
                rowzero.append(i)
                colzero.append(j)
                
    for i in range(rows):
        for j in range(cols):
            if i in rowzero or j in colzero:
                matt[i][j] = 0
    return matt
s1 = matzeros([[3,5,9],[1,0,0],[8,6,3]])
print(s1,end="  ")