# Write a function that computes the volume of a sphere given its radius.
import string
import math


def vol(rad):
    return (4/3) * math.pi * (rad**3)


print('volume', vol(2))

# Write a function that checks whether a number is in a given range (inclusive of high and low)


def ran_check(num, low, high):
    if num > low and num < high:  # if num in range(low,high+1)
        return True
    else:
        return False


print('Is number in range', ran_check(10, 2, 7))
print('Is number in range', ran_check(5, 2, 7))

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.


def up_low(s):
    upperCount = 0
    lowerCount = 0
    for word in s:
        if word.isupper():
            upperCount += 1
        elif word.islower():
            lowerCount += 1
        else:
            pass
    print("No. of Upper case characters : " + str(upperCount))
    print("No. of Lower case Characters : " + str(lowerCount))


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

# Write a Python function that takes a list and returns a new list with unique elements of the first list.


def unique_list(lst):
    temp = []
    for ele in lst:
        if ele not in temp:
            temp.append(ele)
        else:
            pass
    return temp


print('filter arr', unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))

# Write a Python function to multiply all the numbers in a list.


def multiply(numbers):
    multiply = 1
    for num in numbers:
        multiply *= num
    return multiply


print('multiplication', multiply([1, 2, 3, -4]))

# Write a Python function that checks whether a word or phrase is palindrome or not.


def palindrome(s):
    s = s.replace(' ', '')
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


print('is palindrome', palindrome('helleh'))
print('is palindrome', palindrome('nurses run'))

# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)


def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(' ', '').lower()
    for letter in alphabet:
        if letter in str1:
            pass
        else:
            return False
    return True


def ispangram_other(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(' ', '').lower()
    alphabet = set(alphabet)
    str1 = set(str1)
    return str1 == alphabet


print('is pangram', ispangram("The quick Brown fox jumps over the lazy dog"))
print('is pangram', ispangram_other(
    "The quick Brown fox jumps over the lazy dog"))
