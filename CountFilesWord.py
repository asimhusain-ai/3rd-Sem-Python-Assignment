# with open('xyz.txt','r') as file:
#     new = file.read()
#     words = new.split()
#     lines = new.splitlines()
#     char = len(new)
    
# print(new)
# print(words)
# print(lines)
# print(char)


# Frequent Word Count
with open('xyz.txt','r') as file:
    new = file.read()
    words = new.split()
    
dict = {}

for i in words:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
        
for i, count in dict.items():
    print(f"{i}: {count}")
    
    