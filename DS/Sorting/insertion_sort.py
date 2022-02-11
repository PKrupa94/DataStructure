# select one element at a time from the left of the collection
# insert the element at proper position
# after insertion every element to its left will be sorted.
#complexity = O(n^2)

def insertion_sort(arr):
    for index in range(1, len(arr)):
        print('arr', arr)
        currentIndex = index
        currentValue = arr[index]
        while currentIndex > 0 and arr[currentIndex - 1] > currentValue:
            arr[currentIndex] = arr[currentIndex - 1]
            print('arr>>>>>', arr)
            currentIndex -= 1
        arr[currentIndex] = currentValue
    return arr


def insertion_sort_ik(arr, n):
    if n <= 1:
        return
    insertion_sort_ik(arr, n-1)
    last_el = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > last_el:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = last_el
    return arr


a = [3, 5, 8, 7, 6, 9, 2]
# print('insertion sort:', insertion_sort(a))
print('insertion sort:', insertion_sort_ik(a, len(a)))
