# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.


# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


# We want to count each letter in t and store the counts somewhere. Probably a dictionary 
# would make sense. Like dict[letter] = count

# Brute force method is to start with len(s) and check if that satisfies the 
# requirement at index [0:len(s)-1], if not, increment while the second index 
# < len(t)-1
# Then increment the lenght of the substring compared

# Better idea would be to check for indexes in s where letters are not in t
# If not in t, avoid those indices somehow. Depending on the number of those
# letters in the substring we can increase the size of the substring. 

# Brute force is n2 solution
# The solution is just a subset. so two indices. We need to find sometihng better
# than n2. Maybe nlogn? Linear seems impossible. 


# we do not want to recompute the dict everytime. So we 
# input the dict already computed. 

def valid(substring, tdict):
    sdict = {}
    for i in range(len(substring)):
        if substring[i] in tdict:
            sdict[substring[i]] = min(tdict[substring[i]], substring.count(substring[i]))
        else:
            sdict[substring[i]] = substring.count(substring[i])
    return tdict.items() <= sdict.items()


def minWindow(s, t):
    if s == t:
        return s
    tdict = {}
    for i in range(len(t)):
        tdict[t[i]] = t.count(t[i])
    start, substring_length = 0, len(t)
    while substring_length <= len(s):
        while start+substring_length <= len(s):
            print('[', start, ':', start+substring_length, ']')
            print(s[start : start+substring_length])
            if valid(s[start : start+substring_length], tdict):
                return s[start : start+substring_length]
            else:
                start += 1
        start = 0
        substring_length += 1
    return ''

# t = "abcdd"
# tdict = {}
# for i in range(len(t)):
#     tdict[t[i]] = t.count(t[i])
# print(minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))



# After watching neetcode there is a solution in O(n)
# The idea is to start with [0:n], increment n until the requirement is met
# we need to check the requirements in constant time by comparing the last letter
# Then we need to pop the beginning of the substring until it no longer meets the requirement
# Then we increase until it does, and pop the beginning until it doesn't etc



def minWindow(s, t):
    # If the substring is nothing, return nothing
    if t == '': return ''
    # countT is the dict for counting the characters in r
    # window is the same for the substring we compare to t
    countT, window = {}, {}
    # For each character in t, add one to the according key dict value
    # If it doesn't exist, say it's zero
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
    # Have is the number of useful letters in the substring
    # Need is the number of letters in t
    have, need = 0, len(countT)
    # result and result length
    # result is just two pointers
    # result length is the length of the best solution. We initiate to 
    # Infinity because any solution is < than inf
    # And we add a left pointer to 0 because we have the length already. 
    # To find the right pointer, we just add the lenght
    res, resLen, l = [-1,-1], float('infinity'), 0
    # We add each letter of s to the substring until we meet the requirements
    for r in range(len(s)):
        c = s[r]
        # Update the substring dict
        window[c] = 1 + window.get(c, 0)
        # If the letter is in the required dict and the count is the same
        # We add one to have.
        if c in countT and window[c] == countT[c]:
            have += 1
        # Once they are equal (the substring is valid)
        while have == need:
            # If the solution length is less than the current result solution
            if (r-l+1) < resLen:
                # Update the result and result length
                res = [l,r]
                resLen = (r-l+1)
            # Update the substring dict
            window[s[l]] -= 1
            # If the count for substring is less than count for s
            # Decrease have by 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            # increase the left pointer
            l += 1
    # Attribute the result to pointers left and right
    l, r = res[0], res[1]
    # if length of result is less than infinity, return the substring
    # Otherwise return an empty string
    return s[l:r+1] if resLen != float('infinity') else ''


print(minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))