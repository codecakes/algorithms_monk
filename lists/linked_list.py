"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    
    def __getitem__(self, position):
        return self.get_position(position)
    
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        count = 1
        if self.head:
            current = self.head
            while count < position:
                if current.next:
                    current = current.next
                    count += 1
                else:
                    break
            return current
        return None
    
    def __setitem__(self, position, element):
        return self.insert(element, position)
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position - 1 >= 1:
            prev_node = self.get_position(position-1)
        else:
            prev_node = None
        cur_node = self.get_position(position)
        
        if prev_node:
            prev_node.next, new_element.next = new_element, cur_node
        else:
            new_element.next = cur_node
            self.head = new_element

    def __delitem__(self, value):
        self.delete(value)
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current:
            prev = None
            while current.next:
                if current.value == value:
                    if prev:
                        prev.next = current.next
                    else:
                        self.head = current.next
                    del current
                    return
                prev, current = current, current.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
assert ll.head.next.next.value == 3
# Should also print 3
assert ll[3].value == 3

# Test insert
# ll.insert(e4,3)
ll[3] = e4
# Should print 4 now
assert ll[3].value == 4

# Test delete
del ll[1]
# Should print 2 now
assert ll[1].value == 2
# Should print 4 now
assert ll[2].value == 4
# Should print 3 now
assert ll[3].value == 3