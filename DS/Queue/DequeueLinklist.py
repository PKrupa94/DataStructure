
class Node:
    def __init__(self, element, next):
        self._element = element
        self._next = next


class DeQueueLinklist:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def addFirst(self, e):
        newNode = Node(e, None)
        if self.isEmpty():
            self._front = newNode
            self._rear = newNode
        else:
            newNode._next = self._front
            self._front = newNode
        self._size += 1

    def addLast(self, e):
        newNode = Node(e, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear._next = newNode
        self._rear = newNode
        self._size += 1

    def removeFirst(self):
        if self.isEmpty():
            print('Queue is empty')
            return
        ele = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isEmpty():
            self._rear = None
        return ele

    def removeLast(self):
        if self.isEmpty():
            print('Queue is empty')
            return
        p = self._front
        i = 1
        while i < len(self) - 1:
            p = p._next
            i += 1
        self._rear = p
        p = p._next
        e = p._element
        self._rear._next = None
        self._size -= 1
        return e

    def display(self):
        p = self._front
        while p:
            print(p._element, end="-->")
            p = p._next
        print()

    def first(self):
        if self.isEmpty():
            print('Queue is empty')
            return
        return self._front._element

    def last(self):
        if self.isEmpty():
            print('Queue is empty')
            return
        return self._rear._element


Q = DeQueueLinklist()
Q.addFirst(5)
Q.addFirst(3)
print('Queue', Q.display())
Q.addLast(10)
Q.addLast(15)
print('Queue', Q.display())
print('Queue', Q.removeLast())
print('Queue', Q.removeFirst())
print('Queue>>>', Q.display())
