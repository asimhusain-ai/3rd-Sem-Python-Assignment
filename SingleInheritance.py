class A:
    name = "Asim"
    roll = 12
    
class B(A):
    def __init__(self,col):
        self.col = col
        
ob = B("TMU")
print(ob.name)