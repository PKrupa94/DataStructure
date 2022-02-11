def circularPrinter(str):
    dictLetter = {}
    for i, ch in enumerate("1ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        dictLetter[ch] = i
    for c in range(len(str)):
        if c == 0:
            print(min(abs(dictLetter[str[c]]-dictLetter['A']),
                  26-abs(dictLetter[str[c]]-dictLetter['A'])))
        else:
            print(min(abs(dictLetter[str[c]]-dictLetter[str[c-1]]),
                  26-abs(dictLetter[str[c]]-dictLetter[str[c-1]])))


circularPrinter('ZNMD')
