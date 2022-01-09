class Solution:

    def __init__(self):
        self.result = []

    def solveNQueens(self, n: int):
        self.helper(0, n, [])
        result1 = []
        for p in self.result:
            result2 = []
            for k in p:
                temp = ['.' for i in range(n)]
                temp[k] = 'Q'
                result2.append("".join(temp))
            result1.append(result2)
        print('result', result1)
        return result1

    def helper(self, i, n, slate):
        lastQ = len(slate) - 1
        for que in range(lastQ):
            if slate[que] == slate[lastQ]:
                return
            else:
                rowDiff = abs(lastQ-que)
                colDiff = abs(slate[lastQ]-slate[que])
                if rowDiff == colDiff:
                    return
        if i == n:
            self.result.append(slate[:])
            return
        else:
            for col in range(n):
                slate.append(col)
                self.helper(i+1, n, slate)
                slate.pop()
