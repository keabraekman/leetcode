# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".



def backspaceCompare(s,t):
    ss, st, backSpace = '', '', 0
    for i in range(len(s)):
        if s[len(s)-1-i]== '#':
            backSpace += 1
        elif backSpace == 0:
            ss = s[len(s)-1-i] + ss
        else:
            backSpace -= 1

    backSpace = 0
    for i in range(len(t)):
        if t[len(t)-1-i]== '#':
            backSpace += 1
        elif backSpace == 0:
            st = t[len(t)-1-i] + st
        else:
            backSpace -= 1
    return ss == st



def backspaceCompare(s,t):
    l, r = len(s)-1, len(t)-1
    while l >= 0 or r >= 0:
        bl, br = 0,0
        while s[l] == '#':
            bl += 1
            l -= 1
        if bl > 0:
            l -= bl
        else:
            l -= 1

        while t[r] == '#':
            br += 1
            r -= 1
        if br > 0:
            r -= br
        else:
            r -=1

        print(s[l], ' : ', t[r])
        if s[l] != t[r]:
            return False
    return True


print(backspaceCompare("mp","mu#p"))

# print(backspaceCompare("ab#d","abc##d"))