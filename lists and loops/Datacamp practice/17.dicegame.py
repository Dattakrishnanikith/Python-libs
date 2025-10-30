import random

def roll_dice ():
    dice_total = random.randint(1,6) + random.randint(1,6) #lets call this variable dice_total.
    return dice_total


player1 = input("Enter Player 1's Name:\n ")

player2 = input("Enter Player 2's Name:\n ")

roll1 = roll_dice() #with 1 & 6 as the paramteres

roll2 = roll_dice()

print(player1, 'rolled',roll1)

print(player2, 'rolled', roll2)

if (roll1 > roll2):
    print(player1,'wins!')

elif (roll2 > roll1):
    print(player2,"wins!")  

else:
    print('You tie!')      