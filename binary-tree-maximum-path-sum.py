def maxPathSum(root):
    res = [root.val]

    def dfs(root):
        if not root:
            return 0
        leftMax = max(0, dfs(root.left))
        rightMax = max(0,dfs(root.right))
        res[0] = max(res[0], root.val+leftMax+rightMax)
        return root.val+max(leftMax, rightMax)
    dfs(root)
    return res[0]