# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.totalUniCount = 0

    def countUnivalSubtrees(self, root):
        if not root:
            return 0
        self.dfs(root)
        return self.totalUniCount

    def dfs(self, node):
        if not node.left and not node.right:
            self.totalUniCount += 1
            return True
        isAmUni = True
        if node.left:
            isLeftUni = self.dfs(node.left)
            if not isLeftUni or (node.val != node.left.val):
                isAmUni = False
        if node.right:
            isRightUni = self.dfs(node.right)
            if not isRightUni or (node.val != node.right.val):
                isAmUni = False
        if isAmUni:
            self.totalUniCount += 1
        return isAmUni
