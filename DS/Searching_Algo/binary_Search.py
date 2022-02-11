# binary search only works when list(array) is in sorting order
# 1 first we check for the middle element if it match with given element we return it
# 2 if given element < middle element , we search for lower half
# 3 if given element > middle element , we search for upper half

import math
arr = [2, 7, 18, 16, 17, 12, 24]
arr.sort()

# using Iteration


def binarySearch(array, element):
    left_index = 0
    right_index = len(array) - 1
    while left_index <= right_index:
        middle_index = int(math.floor((left_index + right_index)/2))
        if element == array[middle_index]:
            return 'element found at Index', middle_index
        elif element < array[middle_index]:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1
    return 'element not found in list'


print(binarySearch(arr, 7))
print(binarySearch(arr, 24))

# complexity : while loop runs for half of the number n/2 so O(logn)

# using recusrion


def binarySearchRecursion(array, element, left_index, right_index):
    if left_index > right_index:
        return 'element not found'
    else:
        middle_index = int(math.floor((left_index + right_index)/2))
        if element == array[middle_index]:
            return 'element found at Index', middle_index
        elif element < array[middle_index]:
            return binarySearchRecursion(array, element, left_index, middle_index-1)
        else:
            return binarySearchRecursion(array, element, middle_index+1, right_index)


print('recurison method', binarySearchRecursion(arr, 7, 0, len(arr) - 1))


# using list split
def binarySearchListSplit(array, element):
    print('array', array)
    left_index = 0
    right_index = len(array) - 1
    if left_index > right_index:
        return 'element not found'
    else:
        middle_index = int(math.floor((left_index + right_index)/2))
        if element == array[middle_index]:
            return 'element found at Index', middle_index
        elif element < array[middle_index]:
            return binarySearchListSplit(array[:middle_index], element)
        else:
            return binarySearchListSplit(array[middle_index+1:], element)


print('split method', binarySearchListSplit(arr, 7))
