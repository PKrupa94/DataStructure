def permutation(str):
    permutationC(str, "")


def permutationC(str, result):
    if len(str) == 0:
        print(result)
    else:
        for i in range(len(str)):
            subStr = str[0:i] + str[i+1:]
            permutationC(subStr, result+str[i])


# permutation("pau")


def permutation1(str):
    permutationC1(list(str), "", 0)


def permutationC1(str, result, i):
    if i == len(str):
        print(result)
    else:
        hmap = {}
        for j in range(i, len(str)):
            if str[j] not in hmap:
                hmap[str[j]] = 1
                str[j], str[i] = str[i], str[j]
                permutationC1(str, result+str[i], i+1)
                str[j], str[i] = str[i], str[j]


permutation1("paup")
