# see https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
""" 
Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
# naive approach
# def checkBST(root, unique=[]):
#     """
#     - has unique val
#     - has two or less nodes
#     - left_node < root < right_node
    
#     """
#     unique = unique or []
#     if root:
#         if root.data in unique:
#             return False
#         unique.append(root.data)
#         if root.left:
#             if root.left.data in unique:
#                 return False
#             if root.left.data > root.data:
#                 return False
#             if root.left.right:
#                 if root.left.right.data > root.data:
#                     return False
#         if root.right:
#             if root.right.data in unique:
#                 return False
#             if root.right.data < root.data:
#                 return False
#             if root.right.left:
#                 if root.right.left.data < root.data:
#                     return False
#         return checkBST(root.left, unique) and checkBST(root.right, unique)
#     return True

def inOrder(root): 
    return inOrder(root.left) + [root.data] + inOrder(root.right) if root else [root.data] if root else []

def checkBST(root):
    res = inOrder(root)
    return res == sorted(res) == sorted(list(set(res)))