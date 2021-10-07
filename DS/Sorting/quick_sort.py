# divide and conquer approach
# divide the list into subsets based on pivot element (it mean left side elements of pivot smaller than pivot and right side elements are greater than pivot )
# recursively sort subset using quick sort


def getpartitionIndex(arr, lowIndex, highIndex):
    pivot = arr[lowIndex]
    i = lowIndex + 1
    j = highIndex
    while True:
        while i <= j and arr[i] < arr[pivot]:
            i += 1
        while i <= j and arr[j] > arr[pivot]:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[lowIndex], arr[j] = arr[j], arr[lowIndex]
    return j


def quick_sort(arr, lowIndex, highIndex):
    if lowIndex < highIndex:
        partitionIndex = getpartitionIndex(arr, lowIndex, highIndex)
        quick_sort(arr, lowIndex, partitionIndex-1)
        quick_sort(arr, partitionIndex+1, highIndex)


arr = [3, 5, 8, 9, 6, 2]
quick_sort(arr, 0, len(arr)-1)
print('quick sort', arr)
