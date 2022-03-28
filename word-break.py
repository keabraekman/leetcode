# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

def wordBreak(s, wordDict):
    dp = [False]*(len(s)+1)
    dp[len(s)] = True
    for i in range(len(s)-1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]


def wordBreak(s, wordDict):
    dp = [False]*(len(s)+1)
    dp[len(s)] = True
    for i in range(len(s)-1, -1, -1):
        for w in wordDict:
            if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                dp[i] = dp[i+len(w)]
            if dp[i]:
                break
    return dp[0]





















def wordBreak(s,wordDict):
    dp = [False]*(len(s)+1)
    dp[len(s)] = True
    for i in range(len(s)-1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= s and s[i:i+len(w)] == w:
                dp[i] = dp[i+len(w)]
            if dp[i]:
                break
    return dp[0]









<<<<<<< HEAD








def worBreak(s, wordDict):
=======
def wordBreak(s, wordDict):
>>>>>>> 2361a65097acd790b6b676617016a66f3e5c1da8
    dp = [False]*(len(s)+1)
    dp[len(s)] = True
    for i in range(len(s)-1, -1, -1):
        for w in wordDict:
<<<<<<< HEAD
            if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                dp[i] = dp[i+len(w)]
            else:
=======
            if (i+len(w) <= len(s) and s[i:i+len(w)] == w):
                dp[i] = dp[i+len(w)]
            if dp[i]:
>>>>>>> 2361a65097acd790b6b676617016a66f3e5c1da8
                break
    return dp[0]