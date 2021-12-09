class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    head = None
    prevnode = None
    if not l1:
        return l2
    elif not l2:
        return l1
    while l1 and l2:
        if l1.val == l2.val:
            if head is None:
                head = ListNode(l1.val)
                prevnode = head
                newnode = ListNode(l2.val)
                prevnode.next = newnode
                prevnode = newnode
            else:
                newnode1 = ListNode(l2.val)
                prevnode.next = newnode1
                prevnode = newnode1
                newnode2 = ListNode(l1.val)
                prevnode.next = newnode2
                prevnode = newnode2
            l1 = l1.next
            l2 = l2.next
        elif l1.val < l2.val:
            if head is None:
                head = ListNode(l1.val)
                prevnode = head
            else:
                newnode = ListNode(l1.val)
                prevnode.next = newnode
                prevnode = newnode
            l1 = l1.next
        elif l2.val < l1.val:
            if head is None:
                head = ListNode(l2.val)
                prevnode = head
            else:
                newnode = ListNode(l2.val)
                prevnode.next = newnode
                prevnode = newnode
            l2 = l2.next
    while l1:
        newnode = ListNode(l1.val)
        prevnode.next = newnode
        prevnode = newnode
        l1 = l1.next
    while l2:
        newnode = ListNode(l2.val)
        prevnode.next = newnode
        prevnode = newnode
        l2 = l2.next
    return head
