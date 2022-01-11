
import collections


def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    arrStr1 = sorted(str1)
    arrStr2 = sorted(str2)
    str1 = "".join(arrStr1)
    str2 = "".join(arrStr2)
    return str1 == str2


print(checkPermutation('abc', 'cba'))
print(checkPermutation('abc', 'dba'))
print(checkPermutation('abc', 'cbafdffcd'))


def checkPermutation2(str1, str2):
    if len(str1) != len(str2):
        return False
    tempArr = []
    for ch in str1:
        tempArr.append(ch)
    for ch in str2:
        if ch in tempArr:
            tempArr.remove(ch)
    return True if len(tempArr) == 0 else False


print(checkPermutation2('abc', 'cba'))
print(checkPermutation2('abc', 'dba'))
print(checkPermutation2('abc', 'cbafdffcd'))


def checkPermutation3(str1, str2):
    if len(str1) != len(str2):
        return False
    dic1 = collections.Counter(str1)
    dic2 = collections.Counter(str2)
    return dic1 == dic2


print(checkPermutation3('abc', 'cba'))
print(checkPermutation3('abc', 'dba'))
print(checkPermutation3('abc', 'cbafdffcd'))
