
def isBST(root):
    if not root:
        return True
    isBST = True
    return isBST

    def helper(node):
        if not node.left and not node.right:
            return True
        isLeftBST = helper(node.left)
        if not isLeftBST or node.left.val > node.val:
            isBST = False
        isRightBST = helper(node.right)
        if not isRightBST or node.right.val < node.val:
            isBST = False
        return isBST

    helper(root)
