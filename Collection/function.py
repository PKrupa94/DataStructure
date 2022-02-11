# define a function
def display():
    print('Hello,This is my first Python Function')


# calling a function
display()


def add(a, b):
    return a+b


# sum of 2 numbers
sum = add(5, 6)
print('sum', sum)

# sum of multiple numbers


def addNumbers(*a):
    sum = 0
    for num in a:
        sum = sum + num
    return sum


multipleNumSum = addNumbers(1, 4, 5, 7, 9, 10)
print('multipleNumSum', multipleNumSum)

# multiplication


def multiplication(a, b):
    return a*b


multiply = multiplication(12, 3)
print('multiply', multiply)
