class Solution:

    def __init__(self):
        self.result = []

    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        self.helper(candidates, 0, [], target)
        return self.result

    def helper(self, arr, i, slate, target):
        if sum(slate) == target:
            self.result.append(slate[:])
            return
        elif i == len(arr) or sum(slate) > target:
            return
        else:
            count = 0
            for j in range(i, len(arr)):
                if arr[j] != arr[i]:
                    break
                count += 1
            self.helper(arr, i+count, slate, target)
            for p in range(count):
                slate.append(arr[i])
                self.helper(arr, i+count, slate, target)
            for k in range(count):
                slate.pop()
