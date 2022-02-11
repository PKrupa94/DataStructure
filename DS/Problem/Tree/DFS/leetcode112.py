# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    globalBox = False

    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False
        global globalBox
        globalBox = False
        self.dfs(root, targetSum)
        return globalBox

    def dfs(self, node, target):
        if not node.left and not node.right:
            if target == node.val:
                global globalBox
                globalBox = True
        if node.left:
            self.dfs(node.left, target-node.val)
        if node.right:
            self.dfs(node.right, target-node.val)
