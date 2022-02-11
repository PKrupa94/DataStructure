# compare the consecutive element
# if left element is greater than the right element swap them
# continue till the end of the collection and perform serveral passes to sort the elements

a = [3, 5, 8, 7, 6, 9, 2]


def bubbleSort(arr):
    arrLen = len(arr)
    for passes in range(arrLen-1, 0, -1):
        for index in range(passes):
            if arr[index] > arr[index + 1]:
                temp = arr[index + 1]
                arr[index + 1] = arr[index]
                arr[index] = temp
    return arr


print('Bubble sort', bubbleSort(a))


def bubbleSortRecur(arr):
    tempArr = []
    if len(arr) <= 0:
        return []
    for index in range(len(arr)):
        while arr[index] < arr[index - 1]:
            temp = arr[index]
            arr[index] = arr[index - 1]
            arr[index - 1] = temp
    tempArr = bubbleSortRecur(arr[:-1])
    tempArr.append(arr[-1])
    return tempArr


print('Bubble Sort using recursion', bubbleSortRecur(a))
