import random
from tkinter import*



def generate_password():
    letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!', '£', '$', '%', '^', '&', '*', '(', ')', '?', '/', '@']


    nr_letters = int(letter.get())
    nr_numbers = int(number.get())
    nr_symbols = int(symbol.get())

    password_letters = random.choices(letters, k=nr_letters)
    password_numbers = random.choices(numbers, k=nr_numbers)
    password_symbols = random.choices(symbols, k=nr_symbols)

    password = password_letters + password_numbers + password_symbols
    random.shuffle(password)

    password_str = ''.join(password)
    password_label = Label(window, text=f'Password: {password_str}')
    password_label.grid(row=2, column=8)

window = Tk()
window.title('Password Generator')
window.minsize(width=400, height=150)
window.config(padx=20, pady=20)
letter = Entry(window, width=20)
letter.grid(row=1, column=6,)
number = Entry(window, width=20)
number.grid(row=2, column=6,)
symbol = Entry(window, width=20)
symbol.grid(row=3, column=6)

letters_Label = Label(window, text='How many letters do you want')
letters_Label.grid(row=1, column=1)

numbers_Label = Label(window, text='How many numbers do you want')
numbers_Label.grid(row=2, column=1)

symbol_label = Label(window, text='How many symbols do you want')
symbol_label.grid(row=3, column=1)

generate = Button(window, text='Generate password', width=14, height=2, command=generate_password)
generate.grid(row=6, column=4, columnspan=3)


window.mainloop()