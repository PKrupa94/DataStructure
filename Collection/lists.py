# list is collection of same or diffrent data type
#list is mutable in python

I = [34, 67, 9, 78, 23, 76]

# Check length of list
print('Length', len(I))

# sort:sort list in asscending order but only apply to list which has same type elements
I.sort()
print('sort', I)

# reserve:reserve list
I.reverse()
print('reserve', I)

# sum:return sum of element in list
print('sum', sum(I))

# min:return minimum element in list
print('minimum element', min(I))

L = [10, 'Hello', 2.25]

# concate list
C = I + L
print('conconate', C)

# Append:- add element to end of list
L.append('Test')
print('Append', L)

# Insert: add element to perticular index
L.insert(1, 20)
print('After Insert item at index 1', L)

# extend: add multiple items into list
L.extend(['python', 21])
print('Extend list', L)

# delete element from list
del(L[1])
print('list L after Delete', L)

# Slice list
print('slice list', L[0:3])

# copy content of one list to another list
L1 = L[:]
print('copy list', L1)

# split:- split string into lisy
my_str = 'Hello Python'
print('split str', my_str.split())

my_str1 = '12,23,45,56,87,9'
print('split by ,', my_str1.split(','))
