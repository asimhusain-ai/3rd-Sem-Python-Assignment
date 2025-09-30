import random as rd
import string as str

length = 20
char = str.digits + str.ascii_lowercase + str.ascii_uppercase + str.punctuation

password = ''.join(rd.choice(char) for i in range(length))

print(password)