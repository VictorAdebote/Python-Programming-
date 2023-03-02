for number in range(1, 101):  # This is a loop function and there is also range
    if number % 5 == 0 and number % 3 == 0:
        print('FizzBuz')
    elif number % 3 ==0:
        print('Fizz')
    elif number % 5 ==0:
        print('Buzz')
    else:
        print(number)