class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1, l2):
    carry = 0
    total = 0
    node1 = l1
    node2 = l2
    temparr = []
    result = None
    lastNode = None
    while node1 and node2:
        total = node1.val + node2.val + carry
        node1 = node1.next
        node2 = node2.next
        if total >= 10:
            carry = 1
            total = total % 10
        else:
            carry = 0
        temparr.append(total)
    while node1:
        total = node1.val + carry
        node1 = node1.next
        if total >= 10:
            carry = 1
            total = total % 10
        else:
            carry = 0
        temparr.append(total)
    while node2:
        total = node2.val + carry
        node2 = node2.next
        if total >= 10:
            carry = 1
            total = total % 10
        else:
            carry = 0
        temparr.append(total)
    if carry == 1:
        temparr.append(carry)
    for i in temparr:
        if result == None:
            result = ListNode()
            result.val = i
            lastNode = result
        else:
            newNode = ListNode(i)
            lastNode.next = newNode
            lastNode = newNode
    return result


# second

    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        resultNode = lastNode = ListNode(0)
        node1 = l1
        node2 = l2
        while node1 or node2 or carry:
            totalSum = carry
            if node1:
                totalSum += node1.val
                node1 = node1.next
            if node2:
                totalSum += node2.val
                node2 = node2.next
            carry = totalSum // 10
            totalSum = totalSum % 10
            lastNode.next = ListNode(totalSum)
            lastNode = lastNode.next
        return resultNode.next
