# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        if root is None:
            return []
        queue = []
        result = []
        queue.append(root)
        while queue:
            count = len(queue)
            tempArr = []
            for i in range(count):
                node = queue.pop(0)
                tempArr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(tempArr)
        return result
