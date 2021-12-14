class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head):
    stringList = ''
    while(head):
        stringList += str(head.val) + ' -> '
        head = head.next
    print(stringList)
    return stringList

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

import heapq

def mergeKLists(lists):
    # h is an empty heap
    h = []
    for i in range(len(lists)):
        if lists[i]:
            # We add three elements to the heap :
            # Node value, index, and Node
            heapq.heappush(h, (lists[i].val, i, lists[i]))
    # We create two empty linked lists
    rhead = rtail = ListNode(0)
    while h:
        i, n = heapq.heappop(h)[1:]
        rtail.next = n
        rtail = rtail.next
        if n.next:
            heapq.heappush(h, (n.next.val, i, n.next))
    return rhead.next