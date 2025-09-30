from functools import reduce

x = 5

fact = reduce(lambda x,y: x * y, range(1, x+10))
print(fact)