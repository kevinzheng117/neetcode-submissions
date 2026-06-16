class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for p in s:
            if p in match:
                if stack and stack[-1] == match[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return stack == []