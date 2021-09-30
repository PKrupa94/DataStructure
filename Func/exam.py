#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'longestChain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY words as parameter.
#

import collections


def longestChain(words):
    # Write your code here
    words = list(set(words))
    wordlendict = collections.defaultdict(list)

    for word in words:
        wordlendict[len(word)].append(word)

    words = []
    for item, value in sorted(list(wordlendict.items())):
        value.sort()
        words += value

    wordlendict = {}
    maxValue = 0
    for word in words:
        if word in wordlendict:
            continue
        if len(word) == 1:
            wordlendict[word] = 1
            maxValue = max(maxValue, 1)
        else:
            tempc = 0
            for index in range(len(word)):
                tempword = word[:index] + word[index+1:]
                if tempword in wordlendict:
                    tempc = max(tempc, wordlendict[tempword])
            wordlendict[word] = max(tempc+1, 1)
            maxValue = max(maxValue, wordlendict[word])
    return maxValue


longestChain(['anc', 'eds', 'edsea', 'edsewf', 'anec', 'andec'])
