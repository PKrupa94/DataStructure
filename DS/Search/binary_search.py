# firstly binary_search arr must be sort
# check for middle element
# if middle match then return index
# if key < middle element then search for lower half
# if key > middle element then search for upper half

arr = [84, 21, 47, 96, 15, 76]
arr.sort()


def binary_search_iterative(arr, key):
    leftIndex = 0
    rightIndex = len(arr) - 1
    while leftIndex <= rightIndex:
        middleIndex = (leftIndex + rightIndex) // 2
        if key == arr[middleIndex]:
            return middleIndex
        elif key < arr[middleIndex]:
            rightIndex = middleIndex - 1
        elif key > arr[middleIndex]:
            leftIndex = middleIndex + 1
    return 'Element Not Found'


print('binary search', binary_search_iterative(arr, 15))


def binary_search_recursion(arr, key, leftIndex, rightIndex):
    if leftIndex > rightIndex:
        return 'Element Not Found'
    else:
        middleIndex = (leftIndex + rightIndex) // 2
        if key == arr[middleIndex]:
            return middleIndex
        elif key < arr[middleIndex]:
            return binary_search_recursion(arr, key, leftIndex, middleIndex-1)
        elif key > arr[middleIndex]:
            return binary_search_recursion(arr, key, middleIndex+1, rightIndex)


print('binary search interation', binary_search_recursion(arr, 15, 0, len(arr)-1))
