# You are given a string s and an integer k. You can choose any character of 
# the string and change it to any other uppercase English character. You can 
# perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can 
# get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Sliding window problem
def characterReplacement(s, k):
    count_dict, ans, l = dict(), 0, 0
    for r in range(len(s)):
        if s[r] not in count_dict:
            count_dict[s[r]] = 1
        else:
            count_dict[s[r]] += 1

        while (r-l+1) - max(count_dict.values()) > k:
            count_dict[s[l]] -= 1
            l += 1
        ans = max(ans, r-l+1)
    return ans

s = "AABABBA"
k = 1















def characterReplacements(s,k):
    count_dict, ans, l = dict(), 0, 0
    for r in range(len(s)):
        if s[r] not in count_dict:
            count_dict[s[r]] = 1
        else:
            count_dict[s[r]] += 1
        while (r-l+1) - max(count_dict.values()) > k:
            count_dict[s[l]] -= 1
            l += 1
        ans = max(ans, r-l+1)
    return ans

print(characterReplacement(s, k))