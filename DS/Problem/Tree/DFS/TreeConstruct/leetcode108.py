# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, startIndex, endIndex):
        if startIndex > endIndex:
            return None
        midIndex = (startIndex + endIndex) // 2
        rootNode = TreeNode(nums[midIndex])
        rootNode.left = self.helper(nums, startIndex, midIndex-1)
        rootNode.right = self.helper(nums, midIndex+1, endIndex)
        return rootNode
