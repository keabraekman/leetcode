# Serialization is the process of converting a data structure or object into a sequence of 
# bits so that it can be stored in a file or memory buffer, or transmitted across a network 
# connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction 
# on how your serialization/deserialization algorithm should work. You just need to ensure 
# that a binary tree can be serialized to a string and this string can be deserialized to 
# the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary 
# tree. You do not necessarily need to follow this format, so please be creative and come 
# up with different approaches yourself.

 

# Example 1:

# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:

# Input: root = []
# Output: []




# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res, q = '', [root]
        while q:
            level = ''
            for i in range(len(q)):
                node = q.pop(0)
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level += ',' + str(node.val)
                else:
                    level += ',N'
            res += level
        return res[1:]
                
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        res = TreeNode()
        array = []
        for i in range(len(data)):
            element = ''
            while data[i] != ',':
                element += data[i]
            if element == 'N':
                array.append(None)
            else:
                array.append(element)
        
        i, level,q = 0, 1,[]
        while i < len(array):
            for j in range(level):
                q.append(array[j])
            node = TreeNode(array[i])
        

        return array
            
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))