tests = ['babad', 'cbbd', 'a', 'ac', 'ccc']

def longest_palindromic_substring(s):
    answers = []
    for i in range(len(s)):
        center = s[i]
        odd_answer = center
        min_length = min([i, len(s)-i-1])
        j = 1
        for j in range(1,min_length+1):
            if(s[i-j] == s[i+j]):
                odd_answer = s[i-j] + odd_answer + s[i+j]
            else:
                break

        even_answer = ''
        min_length = min([i+1, len(s)-i-1])
        j = 0
        for j in range(0, min_length):
            if(s[i-j] == s[i+j+1]):
                even_answer = s[i-j] + even_answer + s[i+j+1]
            else:
                break
        answers.append(even_answer)
        answers.append(odd_answer)
    return max(answers, key=len)



















def longest_palindromic_substring(s):
    ans = ''
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > len(ans):
                ans = s[l:r+1]
            l -= 1
            r += 1
        l, r = i, i+1
        while l>=0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > len(ans):
                ans = s[l:r+1]
            l -= 1
            r += 1
    return ans









def longest_palindromic_substring(s):
    ans = ''
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > len(ans):
                ans = s[l:r+1]
            l -= 1
            r += 1
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > len(ans):
                ans = s[l:r+1]
            l -= 1
            r += 1
    return ans






# tests = ['babad', "cbbd", 'a', 'ccc']
tests = ['babad']
for i in range(len(tests)):
    print(longest_palindromic_substring(tests[i]))



