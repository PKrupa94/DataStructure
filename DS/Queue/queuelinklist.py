
class Node:
    def __init__(self, element, next):
        self._element = element
        self._next = next


class QueueLinked:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, e):
        newNode = Node(e, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear._next = newNode
        self._rear = newNode
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty')
            return
        ele = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isEmpty():
            self._rear = None
        return ele

    def first(self):
        if self.isEmpty():
            print('Queue is empty')
            return
        return self._front._element

    def display(self):
        p = self._front
        while p:
            print(p._element, end='-->')
            p = p._next
        print()


Q = QueueLinked()
Q.enqueue(10)
Q.enqueue(13)
Q.enqueue(9)
print('Queue:', Q.display())
print(Q.dequeue())
print('Queue:', Q.display())
