x, y = 10, 20
x, y = y,x

print(x,y)

if x > y:
    print(x)
else:
    print(y)

a = 'Hello'
b = 'Bye'
i = len(a)
f = len(b)

if i > f:
    print(a)
else:
    print (b)


for num in range (0,101):
    if num % 2 == 0:
       print(num, end=' ')

i = 0
while i <= 100:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1


rows = 3
columns = 2

for x in range(rows):
    print('*', end='')
    for y in range(columns):
        print('*', end='')
    print('')





