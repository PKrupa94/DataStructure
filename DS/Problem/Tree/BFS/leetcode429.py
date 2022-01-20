
# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node'):
        if root is None:
            return []
        queue = deque()
        result = []
        queue.append(root)
        while queue:
            count = len(queue)
            temp = []
            for _ in range(count):
                node = queue.popleft()
                temp.append(node.val)
                for child in node.children:
                    queue.append(child)
            result.append(temp)
        return result
