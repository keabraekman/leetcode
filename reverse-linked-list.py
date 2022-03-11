def reverseList(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev






















def reverseList(head):
    prev, current = None, head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
