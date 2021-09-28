# map(func,*iterables)

def square(num): return num ** 2


my_nums = [1, 2, 3, 4, 5, 6]


# lamda func

def cube(num): return num**3


print(map(lambda num: num ** 3, my_nums))


for item in map(square, my_nums):
    print('squre', item)

print(list(map(square, my_nums)))  # [1, 4, 9, 16, 25, 36]


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))  # ['EVEN', 'E', 'S']

# filter


def check_even(num):
    return num % 2 == 0


mynums = [1, 2, 3, 4, 5, 6, 7, 8]

print(filter(check_even, mynums))  # [2, 4, 6, 8]
