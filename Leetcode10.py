str = " boss the is Asim"

newstr = str.split()
print(newstr)
i = 0
j = len(newstr) - 1

while i < j:
    temp = newstr[i]
    newstr[i] = newstr[j]
    newstr[j] = temp
    i += 1
    j -= 1
sttr = " ".join(newstr)
print(sttr)