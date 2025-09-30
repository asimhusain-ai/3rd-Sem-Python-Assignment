list = [1,2,3,4,3,2,1]

list1 = list.copy()
print(list1)
rev = list1[::-1]

if list == rev:
    print("Palindromic")
else:
    print("Not Palindromic")