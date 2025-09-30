import math

# a = 100
# x = 20
# print(pow(a,x))
# print(f"{math.sqrt(a):.2f}")
# print(f"{math.sqrt(x):.2f}")

# print(math.lcm(a,x))
# print(math.gcd(a,x))
# print(math.isqrt(a))


# Simple Interest

P = 100000
R = 14
T = 2
si = P*R*T // 100
print(si)

# Compound Interest

P = 100000
R = 14
T = 2
A = P * (1 + R//100) ** T
CI = A - P
print(CI)