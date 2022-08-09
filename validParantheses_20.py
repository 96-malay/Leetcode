# Time: O(N)
# Space: O(N)
def isValid(s):
    stack = []
    dicto = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            if not stack or stack[-1] != dicto[i]:
                return False
            else:
                stack.pop()
    if stack:
        return False
    return True
