# These are the built in functions

# Lambda Function
sum = lambda x,y:  x + y
print("Sum is: ",sum(5 , 9))

# Map Function

l = [2,3,4,6,8,9]
mapped_list = list(map((lambda x: x**3),l))
print("Cube is: ",mapped_list)


# Filter Function

l = [2,3,4,6,8,9]
filtered_list = list(filter((lambda x: x > 2 and x < 6), l))
print("Filtered Data: ",filtered_list)


# Reduce Function

l = [2,3,4,6,8,9]
from functools import reduce
reduced_list = reduce((lambda x,y: x + y),l)
print("Reduced Data: ",reduced_list)
