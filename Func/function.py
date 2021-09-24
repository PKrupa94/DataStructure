# best practic to use function name in snake casing with all lowercase

# def name_of_function():

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

import math


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter


def animal_crackers(text):
    arrStr = text.split()
    if arrStr[0][0] == arrStr[1][0]:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False


def makes_twenty(n1, n2):
    if (n1+n2) == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10))
print(makes_twenty(2, 3))
print(makes_twenty(12, 8))

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name


def old_macdonald(name):
    changeStr = ''
    for index, word in enumerate(name):
        if index == 0 or index == 3:
            changeStr += word.upper()
        else:
            changeStr += word
    return changeStr


print(old_macdonald('macdonald'))

# MASTER YODA: Given a sentence, return a sentence with the words reversed


def master_yoda(text):
    arr = text.split()[::-1]
    # return " ".join(reversed(text.split()))
    return ' '.join(arr)


print(master_yoda('I am home'))
print(master_yoda('We are ready'))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200


def almost_there(n):
    if abs(n-100) <= 10 or abs(n-200) <= 10:
        return True
    else:
        return False


print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.


def has_33(nums):
    for index in range(0, len(nums)-1):
        if nums[index] == 3 and nums[index+1] == 3:
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    returnStr = ''
    for word in text:
        returnStr += 3*word
    return returnStr


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'


def blackjack(a, b, c):
    if (a+b+c) <= 21:
        return a+b+c
    elif (a+b+c) >= 21 and 11 in (a, b, c):
        return (a+b+c) - 10
    else:
        return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    str = '007'
    returnstr = ''
    for index, num in enumerate(nums):
        if num == 0:
            returnstr += '0'
        elif num == 7:
            returnstr += '7'
    if str in returnstr:
        return True
    else:
        return False

# Alternate way
    temparr = [0, 0, 7, 'dummy']
    for num in nums:
        if num == temparr[0]:
            temparr.remove(num)
    return len(temarr) == 1


    #
print(spy_game([1, 2, 4, 0, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.


def summer_69(arr):
    sum = 0
    isElement = False
    for num in arr:
        if num == 6:
            isElement = True
        elif num == 9 and isElement == True:
            isElement = False
        elif isElement == False:
            sum += num
    return sum


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number


def count_primes(num):
    if num <= 3:
        return num-1
    count = 2
    for i in range(4, num):
        prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                prime = False
        if prime:
            count += 1
    return count


print(count_primes(100))
print(count_primes(2))
