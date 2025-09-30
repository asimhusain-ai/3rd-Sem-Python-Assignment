class A:
    name = "Asim"
    
class B:
    roll = 12
    
class C(A,B):
    col = "Tmu"
    
ob = C()
print(ob.name)
print(ob.roll)
print(ob.col)