class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        prev = current = self.root
        while current:
            if current.value == new_val:
                return
            elif new_val < current.value:
                if not current.left:
                    current.left = Node(new_val)
                    return
                else:
                    prev = current
                    current = current.left
            else:
                if not current.right:
                    current.right = Node(new_val)
                    return
                else:
                    prev, current = current, current.right
        return
    
    
    def search(self, find_val):
        return True if self.preorder_search(self.root, find_val) else False
    
    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if not start:
            return
        if start.value == find_val:
            return start
        elif find_val < start.value:
            return self.preorder_search(start.left, find_val)
        else:
            return self.preorder_search(start.right, find_val)
        
    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return "-".join(self.preorder_print(self.root, [])) if self.root else ""

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if not start:
            return
        traversal += ['%s'%start.value]
        self.preorder_print(start.left, traversal)
        self.preorder_print(start.right, traversal)
        return traversal
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
assert tree.search(4) == True
# Should be False
assert tree.search(6) == False