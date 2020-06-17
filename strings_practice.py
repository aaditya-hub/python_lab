import random
from random import choice
import string

first_names = ['Aadi', 'Josh', 'Rick']

last_names = ['Goyal', 'Jones', 'Patel']

address = ['gmail.com','yahoo.com','aol.com']

phone = ['345-567-9876', '324-342-6456', '643-564-7575']

for x in range(100):
    first, last, email = choice(first_names), choice(last_names), choice(address)
    random_name = ('{} {}'.format(first, last))     #f'{first} {last}' (Alternate way of doing this)
    random_email = ('{}.{}@{}'.format(first.lower(), last.lower(), email)) #f'{first.lower()}.{last.lower()}@{email}'
    random_phone = ('{}'.format(choice(phone)))

    print(random_name)
    print(random_email)
    print(random_phone)




