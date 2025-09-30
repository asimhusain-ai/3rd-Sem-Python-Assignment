text = "Asim is a computer science engineer"

str = {}

for i in text:
    if i.isalpha():
        if i in str:
            str[i] += 1
        else:
            str[i] = 1
print(str)