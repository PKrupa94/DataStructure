class Solution:

    def __init__(self):
        self.result = []

    def letterCasePermutation(self, s: str):
        self.helper(s, 0, "")
        return self.result

    def helper(self, st, index, slate):
        if index == len(st):
            self.result.append(slate)
        else:
            if st[index].isdigit():
                self.helper(st, index+1, slate+st[index])
            else:
                self.helper(st, index+1, slate+st[index].lower())
                self.helper(st, index+1, slate+st[index].upper())
