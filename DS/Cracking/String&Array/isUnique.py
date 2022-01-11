def isUnique(str):
    tempDic = {}
    for ch in str:
        if ch not in tempDic:
            tempDic[ch] = 1
        else:
            return False
    return True


str1 = "abcdefg"
str2 = "aabdercs"

# time complexity = O(n)
# space complxity = O(1)

print(isUnique(str1))
print(isUnique(str2))


def isUnique1(str):
    for i in range(len(str)):
        if str[i] in str[i+1:]:
            return False
    return True


print(isUnique1(str1))
print(isUnique1(str2))
