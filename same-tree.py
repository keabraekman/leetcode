
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


def isSameTree(p,q):
    def dfs(p,q):
        if not p and not q:
            return True
        if not p and q or p and not q or p.val != q.val:
            return False
        return (dfs(p.left, q.left) and dfs(p.right, q.right))
    return dfs(p, q)
