add = "1.1.1.1"
new = list(add)
print(new)

for i in range(0, len(new)):
    if new[i] == '.':
        new[i] = '[.]'
        
        
print(new)