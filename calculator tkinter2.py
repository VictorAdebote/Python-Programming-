from tkinter import*
window = Tk()
window.title('Calculator')
window.minsize(width=150, height=250)
window.config(padx=20, pady=20)
calc_open = Entry(window, width=20, justify='right')
calc_open.grid(row=0, column=0, columnspan=4)

def greet():
    pass

def insert(item):
    calc_open.insert(END, item)

def return_():
    equation = calc_open.get()
    answer = eval(equation)
    clear()
    insert(answer)

def clear():
    calc_open.delete(0, END)

button1 = Button(window, text='1', width=3, height=1, command=lambda: insert('1'))
button1.grid(row=1, column=0)

button2 = Button(window, text='2', width=3, height=1, command=lambda: insert('2'))
button2.grid(row=1, column=1)

button3 = Button(window, text='3', width=3, height=1, command=lambda: insert('3'))
button3.grid(row=1, column=2)

button4= Button(window, text='4', width=3, height=1, command=lambda: insert('4'))
button4.grid(row=2, column=0)

button5 = Button(window, text='5', width=3, height=1, command=lambda: insert('5'))
button5.grid(row=2, column=1)

button6 = Button(window, text='6', width=3, height=1, command=lambda: insert('6'))
button6.grid(row=2, column=2)

button7 = Button(window, text='7', width=3, height=1, command=lambda: insert('7'))
button7.grid(row=3, column=0)

button8 = Button(window, text='8', width=3, height=1, command=lambda: insert('8'))
button8.grid(row=3, column=1)

button9 = Button(window, text='9', width=3, height=1, command=lambda: insert('9'))
button9.grid(row=3, column=2)

button10 = Button(window, text='0', width=3, height=1, command=lambda: insert('0'))
button10.grid(row=4, column=0)

button11 = Button(window, text='.', width=3, height=1, command=lambda: insert('.'))
button11.grid(row=4, column=1)

button12 = Button(window, text='c', width=3, height=1, command=clear)
button12.grid(row=4, column=2)

button13= Button(window, text='=', width=5, height=1, command=return_)
button13.grid(row=5, column=1, columnspan=2)

button14 = Button(window, text='*', width=3, height=1, command=lambda: insert('*'))
button14.grid(row=1, column=3)

button14 = Button(window, text='+', width=3, height=1, command=lambda: insert('+'))
button14.grid(row=2, column=3)

button14 = Button(window, text='/', width=3, height=1, command=lambda: insert('/'))
button14.grid(row=3, column=3)

button14 = Button(window, text='-', width=3, height=1, command=lambda: insert('-'))
button14.grid(row=4, column=3)
window.mainloop()