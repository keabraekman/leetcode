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


s = "0P"
print(isPalindrome(s))