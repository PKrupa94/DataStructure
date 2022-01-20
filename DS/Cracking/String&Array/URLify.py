def UrLify(str, strLen):
    result = ""
    for i in range(strLen):
        if str[i] == " ":
            result += "%20"
        else:
            result += str[i]
    return result


print(UrLify("Mr John Smith   ", 13))
