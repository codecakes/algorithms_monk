"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if not head or not head.next:
        return False
    p1 = p2 = n1 = n2 = head
    dct = {}
    
    # check if a loop exists
    while n1.next != n2.next.next and n2.next.next:
        p1, n1 = n1, n1.next
        p2, n2 = n2, n2.next.next
    
    # reached tail - no loop found
    if not n2.next.next:
        return False
    return True

def find_cycle(head):
    if not head or not head.next:
        return False
    p1 = p2 = n1 = n2 = head
    dct = {}
    
    # check if a loop exists
    while n1.next != n2.next.next and n2.next.next:
        p1, n1 = n1, n1.next
        p2, n2 = n2, n2.next.next
    
    # reached tail - no loop found
    if not n2.next.next:
        return False
    
    dct[n1] = (n1.next, p1)
    dct[n2] = (n2.next, p2)
    start = n2
    while n2.next != start:
        p2, n2 = n2, n2.next
        dct[n2] = (n2.next, p2)
    p1, n1 = None, head
    # find the node that creates the loop
    while 1:
        if n1 in dct:
            if dct[n1][1] != p1:
                return dct[n1][1]
        dct[n1] = (n1.next, p1)
        p1, n1 = n1, n1.next