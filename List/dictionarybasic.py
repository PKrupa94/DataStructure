# use when you want to retrive a value based on a key without knowing it's index
# unordered and can not be sorted

d = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}

for key in d:
    print(key)
    print('\n')
    print(d[key])

for item in d.items():
    print(item)

for key, value in d.items():
    print(key)
    print(value)
