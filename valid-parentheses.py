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

print(isValid(s))