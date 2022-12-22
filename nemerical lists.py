# Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for value in range(1, 21):
    print(value)
print()
# Make a list of the numbers from one to one hundred, and then use a for loop to print the numbers
one_hundred=list(range(1, 101))
print(one_hundred)
print()
# Summing a Hundred: Make a list of the numbers from one to one hundred, and then use min() and max() to make sure your list actually starts at one andends at one hundred.
print(f'The minimum in the list {min(one_hundred)}')
print(f'The maximum in the list {max(one_hundred)}')
print(f'The sum of the item in the list {sum(one_hundred)}')
print()
# Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
multiples = []
for numbers in range(3, 31):
    multiples.append(numbers * 3)
print(multiples)
# Cubes: A number raised to the third power is called a cube. For example,the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes
for value in range (1, 11):
    print(value**3)
print()
# Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
list = [values**3 for values in range(1, 11)]
print(list)
