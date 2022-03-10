def isPalindrome(s):
    alphanumericString = ''
    for i in range(len(s)):
        if s[i].isalnum():
            alphanumericString += s[i].lower()
    
    print(alphanumericString)
    for i in range(int(len(alphanumericString)/2)):
        if alphanumericString[i] != alphanumericString[-1-i]:
            return False
    return True
































def isPalindrome(s):
    s = s.lower()
    l,r = 0,len(s)-1
    while l<r:
        while l<r and not s[l].isalnum():
            l+=1
        while r>l and not s[r].isalnum():
            r-=1
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


s = "detartrated"
s = ' '
s= "A man, a plan, a canal: Panama"
print(isPalindrome(s))