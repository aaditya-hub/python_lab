shopping_cart = {'chicken': ('1lbs',11),
                 'Eggs':('1 dozen',4),
                 'Pepper':('1',2),
                 'Banana':('12',4),
                 'Apple':('1',2)
                 }

the_keys = shopping_cart.keys()
the_values = shopping_cart.values()

print('The keys = {}'.format(the_keys))
print('The values = {}'.format(the_values))

sale = {}

for key, value in shopping_cart.items():
    print('The quantity is {} and the price is ${}'.format(value[0],value[1]))
    if value[1] < 10:
        sale.update({key: value[1]})

print("The new dictionary is  \n", sale)

