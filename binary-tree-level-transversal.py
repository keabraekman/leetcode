class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



import collections



def levelOrder(root):
    res = []
    q = collections.deque()
    q.append(root)
    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res