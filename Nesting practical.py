import random
users ={'ultraboy': {'password': '12167', 'email': 'ultraboy@gmail.com', 'fullname': {'first_name': 'Denzel', 'last_name': 'Ojo'}},
        'superboy': {'password': '2369', 'email': 'superboy@gmail.com', 'fullname': {'first_name': 'Victor', 'last_name': 'Adebote'}},
        'okelagirl': {'password': '8745', 'email': 'okelagirl@gmail.com', 'fullname': {'first_name': 'Olivia', 'last_name': 'Ojo'}}
        }
username = input('username: ')
password = input('password: ')

if username in users.keys() and users[username]['password'] == password:
       print('Sigh in successfully')
       print(f'''
       These are your information:
            first name = {users[username]['fullname']['first_name']}
            last name = {users[username]['fullname']['last_name']}
            email = {users[username]['email']}''')
       print('Welcome to game house')
       print('1 for Rock paper scissors\n 2 for Number guessing game')
       users_choice = input('Which game would you like to play?: ')

       if users_choice == '1':
              print('You are now going to play Number guessing game')



              print('''░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ███╗░░░███╗██╗░░░██╗
              ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ████╗░████║╚██╗░██╔╝
              ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ██╔████╔██║░╚████╔╝░
              ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ██║╚██╔╝██║░░╚██╔╝░░
              ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ██║░╚═╝░██║░░░██║░░░
              ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚═╝░░░╚═╝░░░

              ░██████╗░██╗░░░██╗███████╗░██████╗░██████╗██╗███╗░░██╗░██████╗░  ░██████╗░░█████╗░███╗░░░███╗███████╗
              ██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██║████╗░██║██╔════╝░  ██╔════╝░██╔══██╗████╗░████║██╔════╝
              ██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░██║██╔██╗██║██║░░██╗░  ██║░░██╗░███████║██╔████╔██║█████╗░░
              ██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗██║██║╚████║██║░░╚██╗  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
               ╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝██║██║░╚███║╚██████╔╝  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
              ░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝''')
              computers_choice = random.randint(0, 10)
              print('The computer has just chosen a random number between 0 and 9 can you guess what it is?')
              num_of_lives = 3
              while num_of_lives != 0:
                  print(f'{num_of_lives} attempts left')
                  users_choice = int(input('Guess the number: '))
                  if users_choice == computers_choice:
                      print('The user has won')
                      break
                  elif users_choice < computers_choice:

                      print('The user`s choice is too low')
                  else:
                      print('The user`s choice is too high')
                  num_of_lives -= 1

       elif users_choice == '2':
          print('You are now going to play rock, paper, scissors')
          print()



          print('Welcome to Rock, Paper , Scissors')
          options = ['Rock', 'Paper', ' Scissors']
          print()  # Empty print function
          user_input = int(input('What option do you choose. Insert 0 for Rock, 1 for Paper, 2 for Scissors.\n'))
          computers_input = random.randint(0, 2)

          if user_input > 2 or user_input < 0:
              print('Invalid Choice. Game over!')
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
else:
    print('Your sign in is not successful')