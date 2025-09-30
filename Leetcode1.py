def lenoflastword(s):
    return len(s.strip().split()[-1])
obj = lenoflastword("  hello world l lag gye l lag gye mere l lag gaye")
print(obj)