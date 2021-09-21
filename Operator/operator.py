# break : break the loop

a = 0
while a < 5:
    if a == 3:
        break
    a += 1
    print(a)

# pass :
arr = [1, 2, 3, 4, 5, 6]
for i in arr:
    pass
print('pass')

# continue :
for i in arr:
    if i == 3:
        continue
    print(i)

#range : (start,stop,step)

# print number from 0 to 9
for num in range(10):
    print('number', num)

# return even num
for num in range(0, 10, 2):
    print('even number', num)

# enumerate : return item with inedx in tuple form

word = 'abcdef'
for index, item in enumerate(word):
    print(index)
    print(item)

# zip
mylist1 = [1, 2, 3, 4]
mylist2 = ['a', 'b', 'c', 'd']

# use zip in form of list
print(list(zip(mylist1, mylist2)))

# print form of tuple
for item in zip(mylist1, mylist2):
    print(item)
