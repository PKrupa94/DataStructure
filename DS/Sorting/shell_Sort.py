# complexity O(nlog(n))

def shellSort(arr):
    arrLen = len(arr)
    gap = arrLen//2
    while gap > 0:
        i = gap
        while i < arrLen:
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j+gap] = arr[j]
                j = j - gap
            arr[j+gap] = temp
            i = i + 1
        gap = gap // 2
    return arr


a = [3, 5, 8, 7, 6, 9, 2]
print('shell sort', shellSort(a))
