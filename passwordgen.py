import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['#', '@', '&', '*', '!', '%', '$', ',', '+']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print ('''
            _______
    _-_-  _/\______\\__
 _-_-__  / ,-. -|-  ,-.`-.
    _-_- `( o )----( o )-'
           `-'      `-'    
''')
print("\nWelcome to the Speedy Password Generator!\n")

print("Follow the prompts below.\n")

# Collecting user input.

print("How many letters should we include in your password:")
user_letters = int(input("> \n"))

print("How many symbols should we include in your password:")
user_symbols = int(input("> \n"))

print("How many numbers should we include in your password:")
user_numbers = int(input("> \n"))

# Using user input to generate final password/Randomizing user input entries.

final_password = ''

for i in range(0, user_letters + 1):
    final_password += random.choice(letters)
   
for i in range(0, user_symbols + 1):
    final_password += random.choice(symbols)
    
for i in range(0, user_letters + 1):
    final_password += random.choice(numbers)
    
final_password = ''.join(random.sample(final_password, len(final_password)))

print(f"Your new password is: {final_password}.")

    

