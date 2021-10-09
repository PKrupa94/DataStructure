from collections import deque, defaultdict, OrderedDict

d = deque("hello")
print('d', d)
print(d.pop())
print(d.popleft())  # remove element beginning of list
d.extend('456')
print(d)
d.extendleft('h')  # add element beginning of list
print(d)
# rotate element in the list from end
d.rotate(-1)
print('d after rotation', d)

# default dict :
# if key is not present in dic then it will create a key with default given
# value

# limitation : if you create a defaultdict with specific data type and assign a value of other data type it will take it not check for error

i_dct = defaultdict(int)
print(i_dct['key'])
f_dct = defaultdict(float)
print(f_dct['key'])
s_dct = defaultdict(str)
print(s_dct['key'])
a_dict = defaultdict(lambda: 100)
print(a_dict['key'])
arr_dict = defaultdict(list)
arr_dict['key'].append('Hello')
print(arr_dict)
arr_dict['key'].append('World')
print(arr_dict)
dic_dict = defaultdict(dict)
dic_dict['key-1'].update({'Akey': "Hello"})
print(dic_dict)

# ordereddict: maintain order of dict while print dcit

# scoresdict = {'Test1': 10, 'Test2': 20, 'Test3': 30, 'Test4': 40}
scoresdict = [('Test1', 10), ('Test2', 20), ('Test3', 30), ('Test4', 40)]
d = {}
for name, score in scoresdict:
    d[name] = score

print('scoredict before orderdict', d.keys())
print('scoredict before orderdict', d.values())


# print('scoredict before orderdict', scoresdict)
orderscoresdict = OrderedDict(scoresdict)
print('scoredict after orderdict', orderscoresdict.keys())
print('scoredict after orderdict', orderscoresdict.values())
