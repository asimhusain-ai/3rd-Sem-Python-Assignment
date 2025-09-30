def paskaltri(num):
    row = [1]
    for i in range(num):
        newRow = [1]
        for j in range(1,len(row)):
            newRow.append(row[j] + row[j-1])
        newRow.append(1)
        row = newRow
    return row
s1 = paskaltri(5)
print(s1)