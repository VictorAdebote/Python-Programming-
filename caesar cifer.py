from tkinter import*

def caesar():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    new_text = ""
    shift_amount = int(shift.get())
    for letter in caesar_text.get().lower():
        if letter in alphabet:
            position_1 = alphabet.index(letter)

            if shift_amount <= len(alphabet):
                shift_amount = shift_amount % (len(alphabet)-1)

            if message.get().lower()== "encode":
                position_1 = position_1 + shift_amount
                position_1 %= (len(alphabet))

            elif message.get().lower()== "decode":
                position_1 = position_1 - shift_amount

            letter = alphabet[position_1]
            new_text += letter

        else:
            new_text += letter


    Caesar_str = ''.join(new_text)
    alphabet_label = Label(window, text=f'The {message.get().lower()}d text is: "{Caesar_str}"')
    alphabet_label.grid(row=2, column=8)



#direction= input('Input "encode" to encrypt and input "decode" to decrypt:\n')

#caesar_text = input('Input your text:\n')

#Shift_number = input('How many number do you want your encode/decoded text be by:\n')






window = Tk()
window.title('Caesar Cipher')
window.minsize(width=400, height=150)
window.config(padx=20, pady=20)


message_label = Label(window, text='Encode or Decode')
message_label.grid(row=1, column=1)

message = Entry(window, width=20)
message.grid(row=1, column=6)

caesar_label = Label(window, text='Input your Text')
caesar_label.grid(row=2, column=1)

caesar_text = Entry(window, width=20)
caesar_text.grid(row=2, column=6)

shift_number = Label(window, text='shifts number')
shift_number.grid(row=3, column=1)

shift = Entry(window, width=20)
shift.grid(row=3, column=6)

generate = Button(window, text='Generate Caesar', width=14, height=2, command=caesar)
generate.grid(row=6, column=4, columnspan=3)

window.mainloop()