# Given an array of distinct integers candidates and a target integer target, return a list of all 
# unique combinations of candidates where the chosen numbers sum to target. You may return the 
# combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations 
# are unique if the frequency of at least one of the chosen numbers is different.


def combinationSum(candidates, target):
    # The result array starts empty
    res = []

    def dfs(i, cur, total):
        # Base cases : if total == target or if i has reached the end of candidates or if total is greater than target
        if total == target:
            res.append(cur.copy())
            return
        if i>= len(candidates) or total > target:
            return
        # Binary tree. Each node has two branches. 
        #  One where you add i
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        # And one where you don't add i
        cur.pop()
        dfs(i + 1, cur, total)
    dfs(0,[],0)
    return res