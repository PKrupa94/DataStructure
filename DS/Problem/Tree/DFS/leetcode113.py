# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.result = []

    def pathSum(self, root, targetSum: int):
        if not root:
            return []
        self.dfs(root, targetSum, [])
        return self.result

    def dfs(self, node, targetSum, slate):
        slate.append(node.val)
        if not node.left and not node.right:
            if targetSum == node.val:
                self.result.append(slate[:])
        if node.left:
            self.dfs(node.left, targetSum-node.val, slate)
        if node.right:
            self.dfs(node.right, targetSum-node.val, slate)
        slate.pop()
