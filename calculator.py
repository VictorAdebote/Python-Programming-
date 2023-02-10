'''
1. Collect the user input on the tye of operator to be used
2. Collect the users input for 2 integers
3. To perform the operation on the integers in 2 above based on the users choice in 1
4. Print output
'''

print('Welcome to calculator.')  # Welcome statement
print()  
print('''
    0: addition
    1: subtraction
    2: multiplication
    3: division
    4: exponential
''')

operator = input('Choose the corresponding number of the operator to be used from the list above: ')  # This collects input from the user and saves it to the variable operator.
num_1 = int(input('Insert the first number: '))  # This collects input from the user and saves it to the variable name, int is for typecasting.
num_2 = int(input('Insert the second number: '))  # This collects input from the user and saves it to the variable name, int is for typecasting.

if operator == '0':  # Using the if statement to check to the comparison.
   answer = (num_1 + num_2)  # Adding num_1 and num_2
   print()  # Empty print function
   print(f'{num_1} + {num_2} = {answer}')  # Using the print function, formatting string and place holders to display the answer

elif operator == '1':  # Using the elif statement to check to comparison.
    answer = (num_1 - num_2)  # Subtracting num_2 from num_1
    print()  # Empty print function
    print(f'{num_1} - {num_2} = {answer}')  # Using the print function, formatting string and place holder to display the answer

elif operator == '2':  # Using the elif statement to check to comparison.
    answer = (num_1 * num_2)  # Multiplying num_1 and num_2
    print()  # Empty print function
    print(f'{num_1} * {num_2} = {answer}')  # Using the print function, formatting string and place holder to display the answer

elif operator == '3':  # Using the elif statement to check to comparison
    answer = (num_1 / num_2)  # Dividing num_2 from num_1
    print()  # Empty print function
    print(f'{num_1} / {num_2} = {answer}')  # Using the print function, formatting string place holder to display the answer

elif operator == '4':  # Using the elif statement to check to comparison
    answer = (num_1 ** num_2)  # num_1 raised to the power num_2
    print()  # Empty print function
    print(f'{num_1} ^ {num_2} = {answer}')  # Using the print function, formatting string place holder to display the answer