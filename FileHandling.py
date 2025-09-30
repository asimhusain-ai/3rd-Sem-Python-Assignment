# Opening and Reading a file

file = open('abc.txt','r')
print(file.read())
file.close()

# Opening and Reading a file with (with)

with open('abc.txt','r') as file: # When using with , there is no requirement of close() because with used to close the file
    new = file.read()
    print(new)
    

# Writing and appending to file

file1 = open('xyz.txt','w')
print(file1.write('Asim is my Boss'))
file1.close()

# Appending

file2 = open('xyz.txt','a')
print(file2.write(',And i am here'))