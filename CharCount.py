# Word | Char Counter

text = "hello world hello asim world"
word = text.split()
dict = {}

for i in word:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
        
print(dict)