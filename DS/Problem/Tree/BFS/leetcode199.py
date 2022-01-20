# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]):
        if root is None:
            return []
        q = deque()
        result = []
        q.append(root)
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
            # only this chage in template
            result.append(tempArr[-1])
        return result
