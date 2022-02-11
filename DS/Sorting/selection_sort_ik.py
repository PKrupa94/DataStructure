def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = [4, 3, 2, 56, 25, 87, 45, 34]
print(selectionSort(arr))
