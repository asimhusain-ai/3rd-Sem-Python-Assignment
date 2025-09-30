str = "Asim husain is Boss"
str = str.lower()
vowel_count = 0
consonant_count = 0
for i in str:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel_count += 1
    else:
        consonant_count += 1
        
print(vowel_count )
print(consonant_count)