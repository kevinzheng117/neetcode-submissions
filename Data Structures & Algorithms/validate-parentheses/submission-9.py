class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for p in s:
            if p in {"(", "{", "["}:
                stack.append(p)
            else:
                if stack and stack[-1] == match[p]:
                    stack.pop()
                else:
                    return False
        
        return stack == []