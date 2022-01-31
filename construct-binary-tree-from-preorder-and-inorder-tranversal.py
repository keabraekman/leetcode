# Given two integer arrays preorder and inorder where 
# preorder is the preorder traversal of a binary tree 
# and inorder is the inorder traversal of the same tree, 
# construct and return the binary tree.

# Input: 
# preorder = [3,9,20,15,7], 
# inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# The first in preorder is the root
# The second is the left subtree root
# The right is the right subtree root

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])