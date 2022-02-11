def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i = i + 1
        while i <= j and arr[j] > pivot:
            j = j + 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    # swap value with pivot
    arr[low], arr[j] = arr[j], arr[low]
    return j


a = [3, 5, 8, 7, 6, 9, 2]
print('quick sort', quickSort(a, 0, len(a)-1))
