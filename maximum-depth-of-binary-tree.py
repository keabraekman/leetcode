# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node 
# down to the farthest leaf node.

result = []
def maxDepth(root):
    if not root:
        return 0
    result, q = 0, [root]
    while q:
        for i in range(len(q)):
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result += 1
    return result





def maxDepth(root):
    def dfs(root):
        if not root:
            return 0
        return 1+max(dfs(root.left), dfs(root.right))
    return dfs(root)

def maxDepth(self, root):
    if not root:
        return 0
    return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))