class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Given the head of a linked list, remove the nth node from the end of the list 
# and return its head.

def removeNthFromEnd(head, n):
    # We create a dummy node that precedes the head
    dummy = ListNode(0,head)
    # The two pointers. One at the dummy node, the other at the head
    left = dummy
    right = head
    # Separate the two pointers by n
    for i in range(n):
        # Make sure that the Node exists
        if(right):
            right = right.next
    # Go through the linked list
    while(right):
        left = left.next
        right = right.next
    # 'Delete' the node by removing its link
    left.next = left.next.next
    return dummy.next


def removeNthFromEnd(head, n):
    dummy = ListNode(0,head)
    left = dummy
    right = head
    for i in range(n):
        right = right.next
    while(right):
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next
