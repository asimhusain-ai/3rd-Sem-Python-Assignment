class abb:
    def __init__(self, name , roll):
        self.__name = name
        self.roll = roll
    
    def show(self):
        print(self.__name)
    
ob = abb("Asim",12)
ob.show()