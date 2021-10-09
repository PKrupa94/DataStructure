
class stackArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return self._data.pop()

    def top(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return self._data[-1]


s = stackArray()
s.push(2)
s.push(5)

print('s', s._data)
