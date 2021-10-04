# match with each consucutive element and perform swipe
# time complexity : worst case : O(n^2) and best casa when arr is alredy sorted then no need to perform any whipe so O(n)
# after each iteration each part of right side of array will be sorted

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr


arr = [3, 5, 8, 9, 6, 2]

print('bubble sort', bubble_sort(arr))
