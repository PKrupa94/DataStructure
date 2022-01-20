from collections import defaultdict as dic


def oneaway(str1, str2):
    dic1 = dic(int)
    dic2 = dic(int)
    for ch in str1:
        dic1[ch] += 1
    for ch in str2:
        dic2[ch] += 1
    count = 0
    for key, value in dic1.items():
        if value != dic2[key]:
            count += 1
    return True if count <= 1 else False


print(oneaway('pale', 'ple'))
print(oneaway('pales', 'pale'))
print(oneaway('pale', 'bale'))
print(oneaway('pale', 'bake'))
