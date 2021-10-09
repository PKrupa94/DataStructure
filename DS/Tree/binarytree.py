class _Node:

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right


def inorder(troot):
    if troot:
        inorder(troot._left)
        print(troot._element, end=' ')
        inorder(troot._right)


def preorder(troot):
    if troot:
        print(troot._element, end=' ')
        preorder(troot._left)
        preorder(troot._right)


def postorder(troot):
    if troot:
        postorder(troot._left)
        postorder(troot._right)
        print(troot._element, end=' ')


def countnode(troot):
    if troot:
        x = countnode(troot._left)
        y = countnode(troot._right)
        return x + y + 1
    return 0


def heightree(troot):
    if troot:
        x = heightree(troot._left)
        y = heightree(troot._right)
        if x > y:
            return x + 1
        else:
            return y + 1
    return 0


y = _Node(30)
x = _Node(20)
root = _Node(10)

root._left = x
root._right = y
print('inorder', inorder(root))
print('preorder', preorder(root))
print('postorder', postorder(root))
print('totalnode', countnode(root))
print('treeheight', heightree(root))


# class BinaryTree:
#     def __init__(self):
#         self._root = None

#     def maketree(self, e, left, right):
#         self._root = _Node(e, left._root, right._root)

#     def inorder(self, troot):
#         if troot:
#             self.inorder(troot._left)
#             print(troot._element, end=' ')
#             self.inorder(troot._right)

#     def preorder(self, troot):
#         if troot:
#             print(troot._element, end=' ')
#             self.preorder(troot._left)
#             self.preorder(troot._right)

#     def postorder(self, troot):
#         if troot:
#             self.postorder(troot._left)
#             self.postorder(troot._right)
#             print(troot._element, end=' ')


# x = BinaryTree()
# y = BinaryTree()
# z = BinaryTree()
# a = BinaryTree()  # for null left and right

# x.maketree(20, a, a)
# y.maketree(30, a, a)
# z.maketree(10, x, y)
