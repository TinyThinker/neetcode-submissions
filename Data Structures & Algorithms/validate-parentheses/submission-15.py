class Solution:
    def isValid(self, s: str) -> bool:
        # We will be usig a stack. 
        # We will be pushing the character into the stack if it's a left piece.
        # If it a right we will check that the top of the stack is a matching.
        # In order to know what piece we need to match, we will use a dictionary.
        match = {'}':'{', ')':'(', ']':'['}
        stack = []
        for c in s:
            if c in match:
                if not stack or stack.pop() != match[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
