import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']','|',':',';','"',"'",'<','>',',','.','?','/','`','~']

print("Welcome to the password generator")

letter_count = int(input("How many letters would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like in your password?\n"))
number_count = int(input("How many numbers would you like in your password?\n"))

#construct initial passcode using inputs
selected_letters = []
selected_symbols = []
selected_numbers = []

#select letter_count + 1 amount of random letters by randomly generating an index and add it to list
for number in range(1, letter_count + 1):
    selected_letters.append(letters[random.randint(1, len(letters) - 1)])

# do the same for symbols
for number in range(1, symbol_count + 1):
    selected_symbols.append(symbols[random.randint(1, len(symbols) - 1)])

#do the same for numbers
for number in range(1, number_count + 1):
    selected_numbers.append(numbers[random.randint(1, len(numbers) - 1)])

print(selected_letters)
print(selected_symbols)
print(selected_numbers)
#turn arrays into final randomized string

all_values = selected_letters + selected_symbols + selected_numbers

randomized_password = random.sample(all_values, len(all_values))

print("Your password is:")
for value in randomized_password:
    print(value, end='')

















