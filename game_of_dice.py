"""
Game play: to simulate the flipping coin
to have a program to randomly select the side of the coin
give the user the ability to guess the side of the coin

"""

import random

x = random.choice(["Heads","Tails"])
win = 0
lose = 0
Total = 0
while True:

    y = str(input("'Heads', 'Tails' or 'Done' \n"))
    print (y)

    if y == "Done":
        print("Game over")
        print('The number of wins {}'.format(win))
        print('Percentage of correct guesses {} / {} = {}%'
              .format(win, Total, round((win/Total)*100)))
        print('The number of losses {}'.format(lose))
        break

    elif y == x:
        print("You win")
        win += 1

    else:
        print("you lose")
        lose += 1

    Total += 1



