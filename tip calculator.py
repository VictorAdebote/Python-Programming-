print('Welcome to the tip calculator')  # Welcome statement
print()
total_bill = float(input('What is the overall bill £ '))  # overall bill
print()
percentage_tip = int(input('Which percentage tip would you like? 5,10,15,20 '))  # Percentage_tip
print()
num_of_people = int(input('How many people will split the bill '))  # number of people to split the bill

tip = (percentage_tip/100)*total_bill
bill_plus_tip = total_bill + tip
bill_per_person = bill_plus_tip/num_of_people
round_up_bill_per_person = round(bill_per_person, 2)
print()
print(f'Each person should pay: £{round_up_bill_per_person}')