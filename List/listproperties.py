mylist = ['1', '2', '3', '4', '5']
mylist1 = ['6', '7', '8', '9']

# indexing
print(mylist[1])
#output : 2

# slicing
print(mylist[2:])
#output : ['3', '4', '5']

# concat
print(mylist + mylist1)
#output : ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# add new item end of the list
mylist.append('hello')
print(mylist)
#output:['1', '2', '3', '4', '5', 'hello']

# remove item from end of list
mylist.pop()
print(mylist)
#output:['1', '2', '3', '4', '5']

# remove item from any index
print(mylist.pop(1))
#output : 2
print(mylist)
#output : ['1', '3', '4', '5']

# sort list
newlist = ['d', 'a', 't', 'c', 'o', 'w', 'b']
newlist.sort()
print(newlist)
#output : ['a', 'b', 'c', 'd', 'o', 't', 'w']
newlist.reverse()
print(newlist)
#output : ['w', 't', 'o', 'd', 'c', 'b', 'a']

# replace current value with new value at perticular index
newlist[0] = 'k'
print(newlist)
#output : ['k', 't', 'o', 'd', 'c', 'b', 'a']

# insert value at index and move rest of the element to next
newlist.insert(0, 'u')
print(newlist)
#output : ['u', 'k', 't', 'o', 'd', 'c', 'b', 'a']
