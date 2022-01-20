# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        q = deque()
        q.append(root)
        result = []
        isLtoR = False
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
            # ONLY THIS CHANGE TO TEMPLATE
            if isLtoR:
                tempArr.reverse()
            result.append(tempArr)
            isLtoR = not isLtoR
        return result
