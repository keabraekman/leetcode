s = "([)]"

# Given a string s containing just the characters '(', ')', '{', '}', 
# '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.


s= "]"

def isValid(s):
    stack = []
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    for i in range(len(s)):
        if(s[i] in opening):
            stack.append(opening.index(s[i]))
        else:
            if(len(stack) > 0 and closing.index(s[i]) == stack[len(stack)-1]):
                stack.pop()
            else:
                return False
    if(stack):
        return False
    else:
        return True

















def isValid(s):
    stack, open, close = [], {}, {}
    open['('], open['{'], open['['] = 1,2,3
    close[')'], close['}'], close[']'] = 1,2,3
    for i in range(len(s)):
        if s[i] in open:
            stack.append(open[s[i]])
        else:
            if stack and stack[-1] == close[s[i]]:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


s = "]"
print(isValid(s))



