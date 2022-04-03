# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    def dfs(i, minimum, maximum):
        if not i:
            return True
        if i.val < maximum and i.val > minimum:
            return (dfs(i.left, minimum, i.val) and dfs(i.right, i.val, maximum))
        else:
            return False
    return dfs(root, float('-inf'), float('inf'))





def isValidBST(root):
    def dfs(i, minimum, maximum):
        if not i:
            return True
        elif i.val <= minimum or i.val >= maximum:
            return False
        else:
            return (dfs(i.left, minimum, i.val) and dfs(i.right, i.val, maximum))
    return dfs(root, float('-inf'), float('inf'))










def isValidBST(root):
    def dfs(i, minimum, maximum):
        if not i:
            return True
        if i.val <= minimum or i.val >= maximum:
            return False
        else:
            return dfs(i.left, minimum, i.val) and dfs(i.right, i.val, maximum)
    return dfs(root, float('-inf'), float('inf'))















def isValidBST(root):

    def valid(node, left, right):
        if not node:
            return True
        if left<node.val<right:
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        else:
            return False
    
    return valid(root, float('-inf'), float('inf'))










def isvalidBST(root):
    def dfs(node, left, right):
        if not node:
            return True
        if left<node.val<right:
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        else:
            return False
    return dfs(root, float('-inf'), float('inf'))