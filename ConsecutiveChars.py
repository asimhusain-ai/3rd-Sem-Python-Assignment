def consecutivechars(s):
    count = mx = 1
    if not s:
        return 0
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
            mx = max(mx, count)
        else:
            count = 1
            
    return mx

print(consecutivechars("leetcoddeddddeeee"))