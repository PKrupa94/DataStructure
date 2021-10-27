import collections


def frequencySort(nums):
    dic = collections.defaultdict(int)
    for num in nums:
        dic[num] += 1
    sortdic = sorted(dic.items(), key=lambda x: x[1])
    result = []
    temparr = []
    tempcount = 0
    for key, count in sortdic:
        if tempcount == count:
            temparr.append(key)
        else:
            if len(temparr) != 0:
                temparr.sort(reverse=True)
                for num in temparr:
                    result += [num] * tempcount
                temparr = []
            temparr.append(key)
            tempcount = count
    if len(temparr) != 0:
        temparr.sort(reverse=True)
        for num in temparr:
            result += [num] * tempcount
    return result


print(frequencySort([1, 1, 2, 2, 2, 3]))


def frequencySort_other(nums):
    result = []
    dic = collections.Counter(nums).most_common()
    dic.sort(key=lambda x: x[0], reverse=True)
    dic.sort(key=lambda x: x[1])
    for pair in dic:
        num, count = pair
        # result += [num] * count
        result.extend([num] * count)
    return result


print(frequencySort_other([1, 1, 2, 2, 2, 3, 3]))
