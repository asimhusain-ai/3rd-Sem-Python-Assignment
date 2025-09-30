str = "  Asim is the student of tmu and currently he was pursuing btech    "

str = str.strip().split()
list = []

for x in range(len(str)):
    list.append(str[x])
    
print(min(list, key=len))