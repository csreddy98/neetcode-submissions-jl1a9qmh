class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpen = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for i in s:
            if i in closeOpen:
                if stack and stack[-1] == closeOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False