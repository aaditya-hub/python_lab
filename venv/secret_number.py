#########
#secret number
#
#
#
#
#
############

import random

secret_number = random.randint(1,10)

while True:

    user_input = float(input("Enter a number between 1 and 10: \n"))

    if secret_number > user_input:
        print(">")
    elif secret_number < user_input:
        print("<")
    else:
        print("You Win a Million Dollars")
        break



