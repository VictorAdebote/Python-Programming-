import random # This is a file that  contains functions that helps to randomise.

letters = ['a','b','c','d','e','f','g','h', 'i', 'j' , 'k', 'l', 'm','n','o', 'p', 'q', 'r', 's' ,'t' ,'u', 'v' ,'w' ,'x' ,'y' ,'z']  # This is a list of the letters in the alphabet
number =  ['0','1', '2' ,'3', '4' ,'5', '6' ,'7', '8', '9'] # This is a list of numbers
symbols =  ['!', '#', '$' ,'%','&', '+', '-'] # This is a list of symbols

print('Welcome to password generator') # This is a welcome statment
print() # An empty print function for a clear line
num_letters = int(input('How many letters do you want in your password: ' )) # This is an input for how many letters the user wants
print() # An empty print function for a clear line
num_symbols = int(input('How many symbols do you want in your password: ' )) # This is an input for how many symbols the user wants
print() # An empty print function for a clear line
num_number =  int(input('How many numbers do you want in your password: ' )) # This is an input for how many number the user wants

password_letter = [] # This is an empty list that will later contain our randomly chosen letters for our password
for i in range(0,num_letters):
    random_letter = letters[random.randint(0, len(letters)-1)] # It randomly picks the letters from our letters list by picking random index using the randint function
    password_letter.append(random_letter) # It appends the random letter into the empty password_letter list on line 15

password_symbol = [] # This is an empty list that wiil later contain our randomly chosen symbol for our password
for i in range(0,num_symbols):
    random_symbol = symbols[random.randint(0, len(symbols)-1)] # It randomly picks the symbol from out symbol list by picking a random index using the randint function
    password_symbol.append(random_symbol) # It appends the random symbol into the empty password_symbol list on line 20

password_number = [] # This is an empty list that will later contain our randomly chosen number for our password
for i in range(0, num_number):
        random_number = number[random.randint(0, len(number)-1)] # It randomly picks the number from out number list by picking a random index using the randint function
        password_number.append(random_number) # It appends the random number into the empty password_number list on line 25

password = (password_letter+password_symbol+password_number) # Add up all the password_letters, password_symbols and password_number
random.shuffle(password) # This shuffles up the whole password together
pass_word = '' # This is an empty string that will contain all the password items
for i in password :
    pass_word += i # It loops through the password list in line 30 and adds it to the empty string inline 32
print() # An empty print function for a clear line
print(f'Your password is {pass_word}') # Prints out the password