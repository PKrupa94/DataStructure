def strCompression(str1):
    result = ""
    count = 0
    for i in range(len(str1)):
        count += 1
        if (i+1 >= len(str1)) or (str1[i] != str1[i+1]):
            result += str1[i] + str(count)
            count = 0
    return result if len(result) < len(str1) else str1


print(strCompression("aabcccccaaa"))
