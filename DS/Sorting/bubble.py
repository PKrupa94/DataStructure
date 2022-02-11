def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    print(arr)


arr = [10, 4, 98, 34, 56, 86, 2, 45]
print(bubble_sort(arr))
