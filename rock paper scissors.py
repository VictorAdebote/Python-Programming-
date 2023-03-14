import random  # Import random randomizes the number in this code
print('Welcome to Rock, Paper , Scissors')  # Welcome Statement
options = ['Rock', 'Paper', ' Scissors']  # Options for rock, paper, scissors
print()  # Empty print function
user_input = int(input('What option do you choose. Insert 0 for Rock, 1 for Paper, 2 for Scissors.\n'))  # The users input and interger number
computers_input = random.randint(0, 2)  # Using random.randint

if user_input > 2 or user_input < 0:  # Using the is statement
    print('Invalid Choice. Game over!')  # Printing a com
else:
    user_choice = options[user_input]
    computers_choice = options[computers_input]

    print(f'You chose {user_choice}')
    print(f'The computer chose {computers_choice}')

    if user_input == computers_input:
        print('It is a tie')
    elif user_input == 2 and computers_input == 1:
        print('You win!')
    elif user_input == 2 and computers_input == 0:
        print('Computer wins!')
    elif user_input == 0 and computers_input == 2:
        print('Computer wins!')
    elif user_input == 0 and computers_input == 1:
        print('Computer wins!')
    elif user_input == 1 and computers_input == 0:
        print('You win!')
    elif user_input == 1 and computers_input == 2:
        print('Computer wins!')