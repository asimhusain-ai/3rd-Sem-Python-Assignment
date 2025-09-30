<<<<<<< HEAD
def is_palindrome(number):
    # Convert the number to a string for easier manipulation
    num_str = str(number)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Get user input
num = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
=======
def palin(num):
    if int(str(num)[::-1]) == num:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
print(palin(151))
>>>>>>> f9e2422 (Py Program Added)
