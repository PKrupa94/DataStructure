# dictionaries have keys and values
# insted of index we can use key to get perticular value
# key are immutable and unique

D = {'usa': 100, 'uk': 200, 'india': 300}

# fetch all the keys from dic
print('keys', D.keys())

# fetch all values from dic
print('values', D.values())

# length
print('length', len(D))

# membership operator : only key works with it in dic
print('Dic containt value', 'uk' in D)

# get any perticular value from dic using key
l = D['uk']
print('value of l', l)

# add new value to d
D['australia'] = 400
print('new value of dic', D)

# delete value from dic
del(D['india'])
print('D after deleting', D)
