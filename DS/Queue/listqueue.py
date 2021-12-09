class QueueArray:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.isEmpty():
            print('queue is empty')
            return
        return self._data.pop(0)

    def first(self):
        if self.isEmpty():
            print('queue is empty')
            return
        return self._data[0]


Q = QueueArray()
Q.enqueue(3)
Q.enqueue(5)
Q.enqueue(9)
Q.enqueue(12)
print('queue:', Q._data)
print('len:', len(Q))
print(Q.dequeue())
print('queue:', Q._data)
