from collections import defaultdict

def traverse_sum(node, displacement, dct, start_pos = 0):
    if not node:
        return
    if node.data not in dct[displacement]:
        dct[displacement].append(node.data)
    traverse_sum(node.left, displacement-1, dct, start_pos)
    traverse_sum(node.right, displacement+1, dct, start_pos)
    return

def vertical_lines(root, idx=0, dct=None):
    dct = dct or defaultdict(list)
    if not root:
        return
    if idx == 0:
        vertical_lines(root.left, idx-1, dct)
        traverse_sum(root, idx, dct, idx)
        vertical_lines(root.right, idx+1, dct)
    elif idx < 0:
        vertical_lines(root.left, idx-1, dct)
        traverse_sum(root, idx, dct, idx)
    else:
        traverse_sum(root, idx, dct, idx)
        vertical_lines(root.right, idx+1, dct)
    res = dct.items()
    return [sum(x[1]) for x in sorted(res, key=lambda x: x[0])]

        


class Node(object):
    def __init__(self, data):
        # super(Node, self).__init__(data)
        self.data = data
        self.left = self.right = None
        self.parent = None


class Tree(object):
    def __init__(self, node):
        # super(Tree, self).__init__(node)
        self.root = node
    
    def insert(self, node):
        prev = current = self.root
        while current:    
            if node.data < current.data:
                prev, current = current, current.left
            elif node.data > current.data:
                prev, current = current, current.right
            else:
                return
        else:
            if node.data > prev.data:
                prev.right = node
            else:
                prev.left = node
            node.parent = prev
        return

n1,n2,n3,n4,n5 = Node(1), Node(2), Node(4), Node(6), Node(100)

t = Tree(n4)
map(t.insert, [n1,n2,n3,n5])
print t
assert vertical_lines(t.root) == [1,8, 104]
        
        