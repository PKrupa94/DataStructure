class _Node:
    # instance variabble
    __slots__ = '_element', '_next'

    # class method
    def __init__(self, element, next):
        self._element = element
        self._next = next


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0  # number of the element

    def isEmpty(self):
        return self._size == 0

    def addLastNode(self, e):
        newest = _Node(e, None)
        if self.isEmpty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def displayElement(self):
        p = self._head
        while p:
            print(p._element, end=' ')
            p = p._next
        print()


L = LinkedList()
L.addLastNode(7)
L.addLastNode(4)
L.addLastNode(12)
L.addLastNode(15)

L.displayElement()
