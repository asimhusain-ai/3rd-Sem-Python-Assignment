import string

text ="!@#$%^&*(A!@#$%^&*()S!@#$%^&*(I@#$%^&*(M@#$%^&*( !@#$%^&*(M@#$%^&*(E@#$%^&*()R#$%^&*(A @#$%^&*(B$%^&*A$%^&*(A#$%^&*P)))))))))"

clean = ""

for i in text:
    if i not in string.punctuation:
        clean+=i
print(clean)

