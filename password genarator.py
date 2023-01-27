import random

letters = ['a','b','c','d','e','f','g','h', 'i', 'j' , 'k', 'l', 'm','n','o', 'p', 'q', 'r', 's' ,'t' ,'u', 'v' ,'w' ,'x' ,'y' ,'z']
number =  ['0','1', '2' ,'3', '4' ,'5', '6' ,'7', '8', '9']
symbols =  ['!', '#', '$' ,'%','&', '+', '-']

print('Welcome to password generator')
print()
num_letters = int(input('How many letters do you want:' ))
print()
num_symbols = int(input('How many symbols would you like:' ))
print()
num_number =  int(input('How many numbers would you like:'))

password_letter = []
for i in range(0,num_letters):
    random_letter = letters[random.randint(0, len(letters)-1)]
    password_letter.append(random_letter)

password_symbol = []
for i in range(0,num_symbols):
    random_symbol = symbols[random.randint(0, len(symbols)-1)]
    password_symbol.append(random_symbol)
password_number = []
for i in range(0, num_number):
        random_number = number[random.randint(0, len(number)-1)]
        password_number.append(random_number)

password = (password_letter+password_symbol+password_number)
random.shuffle(password)
pass_word = ''
for i in password :
    pass_word += i
print(pass_word)