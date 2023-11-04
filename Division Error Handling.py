#Divison Error Handling
'''Write a Python program that takes two numbers as input from the user and performs division.
Handle the ZeroDivisionError and ValueError exceptions using try and except blocks.'''

print("Enter two numbers")

try:
    num_1 = int(input("What is your first number? "))
    num_2 = int(input("What is your second number? "))
    divison = num_1 / num_2
    print(f'{num_1} / {num_2} = {divison}')
except ValueError:
    print("Please make sure you enter a number next time.")
except ZeroDivisionError:
    print("You can't divide by zero try something else.")

#File Reading with Error Handling:

'''Create a program that attempts to read a file specified by the user. If the 
file doesn't exist, catch the FileNotFoundError exception and print a message indicating that the file was not found.'''

try:
    with open('name3.txt', 'r') as file_object:
        file = file_object.read()
        print(file)
except FileNotFoundError:
    print('File was not found')
#Index Error Handling:

'''Write a program that asks the user to enter a list of numbers. Then, ask the user for an index and attempt to access that index in the list.
 Handle the IndexError exception by displaying a message if the index is out of range.'''

num_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

question_2 = input('Enter an index number: ')
try:
    print(num_1[int(question_2)])

except IndexError:
    print('The index is out of range')

#Key Error Handling:

'''Create a dictionary and ask the user for a key to look up. Use a try and except block to handle the KeyError exception if the key is not found in the dictionary.'''

spy = {'nationality': 'Nigeria', 'country': 'England', 'age': '12', 'Weapon': 'Pistol'}

subject = input("What info about the suspect do you need: ")

try:
    print(f"The info for your request is {spy[subject]}")
except KeyError:
    print(f"There is no info with the '{subject}'.")