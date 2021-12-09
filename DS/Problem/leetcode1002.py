def commonchar(words):
    chararr = list(words[0])
    for word in words[1:]:
        newchararr = []
        for ch in word:
            if ch in chararr:
                newchararr.append(ch)
                chararr.remove(ch)
        chararr = newchararr
    return chararr


words = ["bella", "label", "roller"]
print(commonchar(words))
