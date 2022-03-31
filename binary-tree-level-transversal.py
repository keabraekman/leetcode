class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



import collections



def levelOrder(root):
    # Result array is empty
    res = []
    # q is the list we use to cycle through all the nodes and we initialize it with root
    q = [root]
    # While there is an element in q:
    while q:
        # reset the level array to empty
        level = []
        # For each element in q
        for i in range(len(q)):
            # The current node is the first element in q
            node = q.pop(0)
            # If the node exists
            if node:
                # Add the value of the node to the level array
                level.append(node.val)
                # Add the left and right node to q
                q.append(node.left)
                q.append(node.right)
        # If level is not empty
        if level:
            # Apped the elements of level into the result array
            res.append(level)
    return res

def levelOrder(root):
    res = []
    q = [root]
    while q:
        level = []
        for i in range(len(q)):
            node = q.pop(0)
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res










def levelOrder(root):
    res, q = [], [root]
    while q:
        level = []
        for i in range(len(q)):
            node = q.pop(0)
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res













def levelOrder(root):
    res, q = [], [root]
    while q:
        level = []
        for i in range(len(q)):
            node = q.pop(0)
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res