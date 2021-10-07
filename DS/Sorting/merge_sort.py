# divide and conquer approach
# divide the collection of elements into smaller subsets
# recursively sort the subsets
# combine or merge the result into solution
#complexity : O(nlog(n))


def merge_sort(arr, leftIndex, rightIndex):
    if leftIndex < rightIndex:
        middleIndex = (leftIndex + rightIndex) // 2
        merge_sort(arr, leftIndex, middleIndex)  # left part
        merge_sort(arr, middleIndex+1, rightIndex)  # right part
        merge(arr, leftIndex, middleIndex, rightIndex)
    return arr


def merge(arr, leftIndex, middleIndex, rightIndex):
    i = leftIndex
    j = middleIndex + 1
    k = leftIndex
    temparr = [0] * (rightIndex + 1)
    while i <= middleIndex and j <= rightIndex:
        if arr[i] < arr[j]:
            temparr[k] = arr[i]
            i += 1
        else:
            temparr[k] = arr[j]
            j += 1
        k += 1
    while i <= middleIndex:
        temparr[k] = arr[i]
        i += 1
        k += 1
    while j <= rightIndex:
        temparr[k] = arr[j]
        j += 1
        k += 1
    for i in range(leftIndex, rightIndex+1):
        arr[i] = temparr[i]


arr = [3, 5, 8, 9, 6, 2]
print('merge sort', merge_sort(arr, 0, len(arr)-1))
