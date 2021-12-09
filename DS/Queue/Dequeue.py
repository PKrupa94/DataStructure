from typing import DefaultDict


class DEQueueArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0

    # add element beginning of queue
    def addFirst(self, ele):
        self._data.insert(0, ele)

    # add element at last of queue
    def addLast(self, ele):
        self._data.append(ele)

    # remove first element
    def removeFirst(self):
        if self.isEmpty():
            print('DEQueue is empty')
            return
        return self._data.pop(0)

    # remove last element
    def removeLast(self):
        if self.isEmpty():
            print('DEQueue is empty')
            return
        return self._data.pop()

    # return first element from Dequeue
    def first(self):
        if self.isEmpty():
            print('DEqueue is empty')
            return
        return self._data[0]

    # return last element from Dequeue
    def last(self):
        if self.isEmpty():
            print('DEqueue is empty')
            return
        return self._data[-1]


Q = DEQueueArray()
Q.addFirst(10)
Q.addLast(5)
print('QUEUE:', Q._data)
Q.addFirst(11)
Q.addFirst(12)
print('QUEUE:', Q._data)
print('First', Q.removeFirst())
print('QUEUE:', Q._data)
print('Last', Q.removeLast())
