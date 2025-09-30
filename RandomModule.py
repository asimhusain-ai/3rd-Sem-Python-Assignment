import random

print(random.random())
print(random.randint(1, 10))

list = [4, 6, 2, 4,5, 7,9]

random.shuffle(list)
print(list)

print(random.choice(list))