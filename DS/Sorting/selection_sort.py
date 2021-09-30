# Selection sort with unsorted array
# select first element and replace with small one
# This is only sorting which use O(n) swap which is very less than other sorting
#complexity = O(n^2)

def selection_sort(arr):
    for i in range(len(arr)-1):
        swipeIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[swipeIndex]:
                swipeIndex = j
        arr[i], arr[swipeIndex] = arr[swipeIndex], arr[i]
    return arr


arr = [3, 5, 8, 9, 6, 2]
print('selection sort', selection_sort(arr))
