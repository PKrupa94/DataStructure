# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.dfs(root)
        return self.diameter

    def dfs(self, node):
        if not node.left and not node.right:
            return 0
        myDiameter = 0
        leftNodeHight = 0
        rightNodeHight = 0
        if node.left:
            leftNodeHight = self.dfs(node.left)
            myDiameter += leftNodeHight + 1
        if node.right:
            rightNodeHight = self.dfs(node.right)
            myDiameter += rightNodeHight + 1
        self.diameter = max(self.diameter, myDiameter)
        return max(leftNodeHight, rightNodeHight) + 1
