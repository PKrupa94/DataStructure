class _Node:
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._right = right
        self._left = left


class BinarySearchTree:

    def __init__(self):
        self._root = None

    def insertionNode(self, troot, e):
        temp = None
        while troot:
            temp = troot  # return parent of node which we want to insert
            if e == troot._element:
                return
            elif e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right
        n = _Node(e)
        if self._root:
            if e < temp._element:
                temp._left = n
            else:
                temp._right = n
        else:
            self._root = n

    def searchNodeInBinaryTree(self, troot, e):
        while troot:
            if e == troot._element:
                return True
            elif e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right
        return False

    def searchNodeInBinaryRecursion(self, troot, e):
        if troot:
            if e == troot._element:
                return True
            elif e < troot._element:
                return self.searchNodeInBinaryRecursion(troot._left, e)
            elif e > troot._element:
                return self.searchNodeInBinaryRecursion(troot._right, e)
        else:
            return False

    def inoder(self, troot):
        if troot:
            self.inoder(troot._left)
            print(troot._element, end=" ")
            self.inoder(troot._right)


B = BinarySearchTree()
B.insertionNode(B._root, 50)
B.insertionNode(B._root, 30)
B.insertionNode(B._root, 80)
B.insertionNode(B._root, 10)
B.insertionNode(B._root, 40)
B.insertionNode(B._root, 60)
B.inoder(B._root)
print(B.searchNodeInBinaryTree(B._root, 100))
print(B.searchNodeInBinaryTree(B._root, 60))

# print(B.inoder(B._root))
