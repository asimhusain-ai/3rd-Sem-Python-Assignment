# Replace with any specific val

# num = [1,2,3,4,5,6,7,8,9]
# for i in range(len(num)):
#     if num[i] % 2 == 0:
#         num[i] = 3
# print(num)



# Replecing even With Odd

# num = [1,2,3,4,5,6,7,8,9]

# odd = []
# for i in num:
#     if i % 2 != 0:
#         odd.append(i)
        
# result = []
# idx = 0

# for x in num:
#     if x % 2 == 0:
#         result.append(odd[idx % len(odd)])
#         idx += 1
#     else:
#         result.append(x)
# print(result)


# Replecing odd with even

num = [1,2,3,4,5,6,7,8,9]

even = []
for i in num:
    if i % 2 == 0:
        even.append(i)
        
result = []
idx = 0

for x in num:
    if x % 2 != 0:
        result.append(even[idx % len(even)])
        idx += 1
    else:
        result.append(x)
print(result)