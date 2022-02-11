x = int(input('Enter Value X: '))
y = int(input('Enter Value Y: '))

if x > y:
    print('X is greater than Y')
else:
    print('Y is greater than X')

# nested if else
if x >= y:
    if x == y:
        print('X and Y both are equal')
    else:
        print('X is greater than Y')
else:
    print('Y is greater than X')

# elif statement

if x > y:
    print('X is greater than Y')
elif x < y:
    print('X is less than Y')
else:
    print('X and Y both are equal')
