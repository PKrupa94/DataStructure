import collections


def arraysIntersection(arr1, arr2, arr3):
    count1 = collections.Counter(arr1)
    count2 = collections.Counter(arr2)
    count3 = collections.Counter(arr3)
    result = []
    for key in count1.keys():
        if key in count2 and key in count3:
            result.append(key)
    return result

# 3 pointer approach


def arraysIntersection1(arr1, arr2, arr3):
    result = []
    i, j, k = 0, 0, 0
    while i <= len(arr1)-1 and j <= len(arr2)-1 and k <= len(arr3)-1:
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        else:
            if arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] <= arr3[k]:
                j += 1
            else:
                k += 1
    return result
