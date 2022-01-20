# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []
        q = deque()
        q.append(root)
        result = []
        while q:
            qCount = len(q)
            tempArr = []
            for _ in range(qCount):
                node = q.popleft()
                tempArr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(tempArr)
        # only this change in template
        result.reverse()
        return result
