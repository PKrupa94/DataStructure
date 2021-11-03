def merge_sorted_arr(arr1, arr2):
    i = len(arr1) - 1
    j = len(arr2) - 1
    k = j-i-1
    while i >= 0 and j >= 0 and k >= 0:
        if arr1[i] < arr2[k]:
            arr2[k], arr2[j] = arr2[j], arr2[k]
            k -= 1
        else:
            arr2[j] = arr1[i]
            i -= 1
        j -= 1
    while i >= 0:
        arr2[j] = arr1[i]
        i -= 1
        j -= 1
    return arr2


n = 3
arr1 = [1, 3, 5]
arr2 = [2, 4, 6, 0, 0, 0]
# Output: arr2 = [1,2,3,4,5,6]
print(merge_sorted_arr(arr1, arr2))
