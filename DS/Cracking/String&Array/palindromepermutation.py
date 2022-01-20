import collections


def palindromepermutation(str):
    tempDic = collections.Counter(str.lower().replace(" ", ""))
    tempCount = 0
    print(tempDic)
    for key, value in tempDic.items():
        if value == 1:
            tempCount += 1
    return True if tempCount <= 1 else False


print(palindromepermutation("Tact Coa"))
