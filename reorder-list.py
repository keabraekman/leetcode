# You are given the head of a singly linked-list. The list can be represented as

# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Two pointer problem

def reorderList(head):
    # we do this to find the middle of the linked list. one slow and one fast pointer
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Separate the linked list into two linked lists
    second = slow.next
    prev = slow.next = None
    # This reverses the second LinkedList
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    first, second = head, prev
    # Merges both linked lists together
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2 



