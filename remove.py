# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
    
def remove_kth_from_end(head, k):
    curr = head
    numnodes = 0
    while curr is not None:
        if curr.value != k:
            break
        curr = curr.next
        numNodes += 1
    
    new_head = curr
    prev = None
    while curr is not None:
        if curr.value == k:
            if prev is not None:
                prev.next = curr.next
            curr = curr.next
            continue
        prev = curr
        curr = curr.next
    return new_head