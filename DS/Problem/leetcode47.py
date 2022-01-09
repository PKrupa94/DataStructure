class Solution:

    def __init__(self):
        self.result = []

    def permuteUnique(self, nums):
        self.helper(nums, 0, [])
        return self.result

    def helper(self, nums, i, slate):
        if i == len(nums):
            self.result.append(slate[:])
        else:
            hmap = {}
            for pick in range(i, len(nums)):
                print("hmap", hmap)
                if nums[pick] not in hmap:
                    hmap[nums[pick]] = 1
                    nums[pick], nums[i] = nums[i], nums[pick]
                    slate.append(nums[i])
                    self.helper(nums, i+1, slate)
                    slate.pop()
                    nums[pick], nums[i] = nums[i], nums[pick]
