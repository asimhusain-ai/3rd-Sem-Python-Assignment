class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc
        
    def debit(self, amt):
        self.bal -= amt
        print("Rs",amt,"debited from your bank account XXX1234")
        print("\nBalance: ",self.tot(),"\n")
        
    def credit(self, amt):
        self.bal += amt
        print("Rs",amt,"credited to your bank account XXX1234")
        print("\nBalance: ",self.tot(),"\n")
        
    def tot(self):
        return self.bal
        
ob1 = Account(10001,1234)
print("\nB A L A N C E : ",ob1.bal)
print("\nA C C O U N T : ",ob1.acc,"\n\n")
ob1.debit(100)
ob1.credit(1000)