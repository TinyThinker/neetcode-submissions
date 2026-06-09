class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)

            if c == ")" or c == "}" or c == "]":
                try:
                    if self.opposite(stack.pop()) != c:
                        return False
                except Exception:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

    def opposite(self, s: str) -> str:
        if s == '(':
            return ')'
        if s == '[':
            return ']'
        if s == '{':
            return '}'
        return None



        