from enum import unique


s = 'abcdessfkweofiewf'
def lengthOfLongestSubstring(s):
    lengths = []
    for i in range(len(s)):
        substring = ''
        length = 0
        for j in range(i, len(s)):
            if(s[j] not in substring):
                substring += s[j]
                length += 1
            else :
                break
        lengths.append(length)
    if(len(lengths) == 0):
        return 0
    else:
        return max(lengths)






def lengthOfLongestSubstring(s):
    uniqueString, maxLength = '', 0
    for i in range(len(s)):
        if s[i] not in uniqueString:
            uniqueString += s[i]
        else:
            uniqueString = uniqueString[uniqueString.index(s[i])+1:] + s[i]
        maxLength = max(maxLength, len(uniqueString))
    return maxLength




s = 'abcdessfkweofiewf'
# s = "aab"
# s= "dvdf"
# s="aabaab!bb"


print(lengthOfLongestSubstring(s))
