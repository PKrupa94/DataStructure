# select the minimum element and place to the appropriate position
# start to put from least most position
# selection sort is unstable algorothm because it change the order of equal element
#complexity = O(n^2)


def selectionSort(array):
    arrLen = len(arr)
    for currentIndex in range(arrLen - 1):
        for nextIndex in range(currentIndex+1, arrLen):
            if array[nextIndex] < array[currentIndex]:
                temp = array[currentIndex]
                array[currentIndex] = array[nextIndex]
                array[nextIndex] = temp
    return array


arr = [4, 3, 2, 56, 23, 87, 45, 89]
print('Sortded Array using selection sort', selectionSort(arr))
