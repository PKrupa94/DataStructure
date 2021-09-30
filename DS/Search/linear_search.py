def liner_search(arr, key):
    index = 0
    while index < len(arr):
        if arr[index] == key:
            return index
        else:
            index += 1
    return 'Element Not Found'


arr = [84, 21, 47, 96, 15, 76]
print(liner_search(arr, 47))
print(liner_search(arr, 90))
