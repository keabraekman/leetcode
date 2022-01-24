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

t = "abcdd"
tdict = {}
for i in range(len(t)):
    tdict[t[i]] = t.count(t[i])
print(minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))