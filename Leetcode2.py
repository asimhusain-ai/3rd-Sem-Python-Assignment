n = 15

if n <= 0:
    print("Falsi")

while n > 1:
    if n % 3 != 0:
        print("Falsi")
    n = n // 3
print("Trui")