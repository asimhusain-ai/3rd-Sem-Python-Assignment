<<<<<<< HEAD
def swap(x,y):
    temp=x
    x=y
    y=temp
    return x,y
x=int(input("Enter x Value:-"))
y=int(input("Enter y Value:-"))
print("Before:- ",x," ",y)
swapping = swap(x,y)
print("After:- ",swapping)
=======
def swap(a,b):
    a, b = b, a
    return a, b
print(swap(5, 7))
>>>>>>> f9e2422 (Py Program Added)
