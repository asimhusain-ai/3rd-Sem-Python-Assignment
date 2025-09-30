arr = [1,1,1,1,1,0,0,1,0,1,0]

# num = int("".join(map(str, arr)), 10)
# print(num)

num= 0

for i in arr:
    num = num * 2 + i
    
print(num)