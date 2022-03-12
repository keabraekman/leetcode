# Definition for singly-linked list.
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


# def mergeTwoLists(l1, l2):
    # dummy = cur = ListNode(0)
    # while l1 and l2:
    #     if l1.val < l2.val:
    #         cur.next = l1
    #         l1 = l1.next
    #     else:
    #         cur.next = l2
    #         l2 = l2.next
    #     cur = cur.next
    # cur.next = l1 or l2
    # printList(dummy.next)
    # return dummy.next
            

def mergeTwoLists(list1, list2):
    current = ListNode(0)
    dummy = current
    while(list1 and list2):
        if(list1.val <= list2.val):
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if(list1 is None):
        current.next = list2
    else:
        current.next = list1
    return dummy.next


list1 = ListNode(0, ListNode(1, ListNode(4)))
list2 = ListNode(2, ListNode(6))


mergeTwoLists(list1, list2)



def mergeTwoLists(list1, list2):
    res = ListNode(0)
    dummy = res
    while list1 or list2:
        if not list2 or (list1 and list1.val < list2.val):
            res.next = list1
            list1 = list1.next
        elif not list1 or (list2 and list2.val <= list1.val):
            res.next = list2
            list2 = list2.next
        res = res.next
    return dummy.next