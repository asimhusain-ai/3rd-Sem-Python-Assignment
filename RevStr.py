def revstr(str):
    result_str = ""
    
    for ch in str:
        result_str = ch + result_str
    return result_str

print(revstr("misA"))

# def revstr(str):
#     return str[::-1]
# print(revstr("misa"))