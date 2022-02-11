# Definition for a binary tree node.
from collections import OrderedDict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):

        def helper(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd:
                return None
            if preStart == preEnd:
                return TreeNode(preorder[preStart])
            rootNode = TreeNode(preorder[preStart])
            rootIndex = hmap[preorder[preStart]]
            lenLeftPart = rootIndex - inStart
            rootNode.left = helper(
                preStart+1, preStart+lenLeftPart, inStart, rootIndex-1)
            rootNode.right = helper(
                preStart+lenLeftPart+1, preEnd, rootIndex+1, inEnd)
            return rootNode

        hmap = {}
        for i in range(len(inorder)):
            hmap[inorder[i]] = i

        return helper(0, len(preorder)-1, 0, len(inorder)-1)
