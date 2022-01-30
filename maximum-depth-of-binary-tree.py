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




    def dfs(root, result):
        if root.left or root.right:
            result.append(1)
            if root.left:
                dfs(root.left, result)
            if root.right:
                dfs(root.right, result)
        return result

    result = dfs(root, [])
    return result