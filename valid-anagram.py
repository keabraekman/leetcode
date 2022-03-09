# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.


def isAnagram(s,t):
    letterdict = dict()
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] in letterdict:
            letterdict[s[i]] += 1
        else:
            letterdict[s[i]] = 1
        if t[i] not in letterdict:
            letterdict[t[i]] = -1
        else:
            letterdict[t[i]] -= 1
    for i in letterdict:
        if letterdict[i] != 0:
            return False
    return True

def isAnagram(s,t):
    s.sort()
    t.sort()
    return s == t


def isAnagram(s,t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] in t:
            t.remove(s[i])
    return t == ''