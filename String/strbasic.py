# String Properties
# strings are immutable in python(meaning you can't use indexing to change individual elements of a string)

# declare str
mystring = 'Hello World'
mystring = "Hello World"
print(mystring)

# indexing
print(mystring[1])  # return character at index 1

# return last character
print(mystring[-1])

# conver string to upper case
print(mystring.upper())
mystring.lower(
)

# Conver Sting to List
print(mystring.split())

string = 'Hi this is a string'
# split the sting till  i
print(string.split('i'))  # ['H', ' th', 's ', 's a str', 'ng']

# Slice[start:stop:step]
mystr = "dsfbsjfbkewuhweh"

# slice a string at index 2
print(mystr[2:])   # fbsjfbkewuhweh

# slice a string from index 2 to 6 but exclude character at index 6
print(mystr[2:6])  # fbsj

# return slice string from 2 to 8 and jump step of 2
print(mystr[2:8:2])  # fsf

# reverse string
print(mystr[::-1])

# string concatination
print(mystr + mystring)

# print letter more than one time
letter = 'p'
print(letter * 5)

# string formating with format method
print('This is a string {}'.format('INSERT'))  # This is a string INSERT
print('The {} {} {}'.format('fox', 'brown', 'quick'))  # The fox brown quick
# arrange sting based on index >>  The quick brown fox
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
# using keywords >>  The quick brown fox
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))


# floating point format = {value:width(whitespace):precision f}
floatNum = 104.3459353346436346323
print(floatNum)
print('This number was {}'.format(floatNum))
print('This number was {r:1.3f}'.format(r=floatNum))
# output: This number was 104.346
print('This number was {r:10.3f}'.format(r=floatNum))
# output: This number was    104.346
