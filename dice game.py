import random
dice1 = random.randrange(1,7)
dice2 = random.randrange(1,7)

total = dice1+dice2
while (total != 12):
    print('You Failed!! You got', total, 'You need 12 to win!')
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    total = dice1 + dice2
print('You won', total)