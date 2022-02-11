
arr = [24,76,446,34,9,77,54]

def linerSearch(array,element):
    #enumerate give element with index
    for index,value in enumerate(array):
        if value == element:
            return 'element found at Index:',index
    return 'element not found'

print(linerSearch(arr,100))

def liSearch(array,element):
    #range only give index of array
    for i in range(len(array)):
        if array[i] == element:
            return 'element found at Index:',i,element
    return 'element not found'

print(liSearch(arr,9))

def linerSearchUsingWhile(array,element):
    i = 0 # O(1)
    while i < len(array): # O(n+1)
        if array[i] == element: # O(n)
            return 'element found at Index:',i # O(1)
        i += 1
    return 'element not found' # O(n) 

print('While result',linerSearchUsingWhile(arr,34))

#Time complexity = O(n) liner time complexity