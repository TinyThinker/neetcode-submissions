class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        opening = {"{", "(", "["}
        matching = {"{": "}", "(" : ")", "[" : "]" }

        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if stack and c == matching.get(stack[-1], "X"):
                    stack.pop()
                else:
                    return False

        return True if not stack else False


        