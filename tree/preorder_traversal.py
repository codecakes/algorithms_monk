class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return True if self.preorder_search(self.root, find_val) else False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return "-".join(self.preorder_print(self.root, [])) if self.root else ""

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if not start:
            return
        if start.value == find_val:
            return start
        return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if not start:
            return
        traversal += ['%s'%start.value]
        self.preorder_print(start.left, traversal)
        self.preorder_print(start.right, traversal)
        return traversal

if __name__ == "__main__":    
    # Set up tree
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    # Test search
    # Should be True
    assert tree.search(4) == True
    # Should be False
    assert tree.search(6) == False

    # Test print_tree
    # Should be 1-2-4-5-3
    assert tree.print_tree() == '1-2-4-5-3'