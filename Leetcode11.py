a = "1001111"
b = "1101010"

int_a = int(a, 2)
int_b = int(b, 2)
sum = int_a + int_b
new = bin(sum)[2:]
print(new)