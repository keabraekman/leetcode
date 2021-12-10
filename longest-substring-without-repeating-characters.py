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