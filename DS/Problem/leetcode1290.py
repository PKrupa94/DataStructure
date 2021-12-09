# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        node = head
        data = []
        output = 0
        while node:
            data.append(node.val)
            node = node.next
        data.reverse()
        for index, num in enumerate(data):
            output += pow(2, index) * num
        return output
