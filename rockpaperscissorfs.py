computer_choice = 'scissors'

user_choice = input('do you want rock , paper , or scissors?')

if computer_choice == user_choice:
    print('Tie')

elif user_choice == 'rock' and computer_choice == 'scissors':
    print('Win')

elif user_choice == 'paper' and computer_choice == 'rock':
    print('Win')

elif user_choice == 'scissors' and computer_choice == 'paper':
    print('Win')

else:
    print('You lose,computer winsss')
