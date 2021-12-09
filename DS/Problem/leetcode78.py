class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums):
        self.helper(nums, 0, [])
        return self.result

    def helper(self, nums, i, slate):
        if i == len(nums):
            self.result.append(slate[:])
        else:
            self.helper(nums, i+1, slate)
            slate.append(nums[i])
            self.helper(nums, i+1, slate)
            slate.pop()
