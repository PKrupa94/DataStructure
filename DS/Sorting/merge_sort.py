# Devide the collection of elements into smaller subsets
# Recursively sort the subset
# combine or merge the result in solution
# devide and conquer approach

def mergeSort(arr, leftIndex, rightIndex):
    if leftIndex < rightIndex:
        midIndex = (leftIndex+rightIndex) // 2
        mergeSort(arr, leftIndex, midIndex)
        mergeSort(arr, midIndex+1, rightIndex)
        merge(arr, leftIndex, midIndex, rightIndex)
    return arr


def merge(arr, leftIndex, midIndex, rightIndex):
    print('arr', arr)
    i = leftIndex  # use for one half of the arr
    j = midIndex + 1  # use another half of the arr
    k = leftIndex  # for temp arr(which use for merge element) index
    tempArr = [0] * (rightIndex + 1)
    while i <= midIndex and j <= rightIndex:
        if arr[i] < arr[j]:
            tempArr[k] = arr[i]
            i += 1
        else:
            tempArr[k] = arr[j]
            j += 1
        k += 1
    # check any element left in left sub array
    while i <= midIndex:
        tempArr[k] = arr[i]
        i += 1
        k += 1
    # check any element left in right sub array
    while j <= rightIndex:
        tempArr[k] = arr[j]
        j += 1
        k += 1
    print('tempArr', tempArr)
    # move element from temp to actual arr
    for m in range(leftIndex, rightIndex+1):
        arr[m] = tempArr[m]
    print('return arr', arr)
    return arr


a = [3, 5, 8, 7, 6, 9, 2]
print('merge sort', mergeSort(a, 0, len(a)-1))
