class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                print(f"R *** l = {left}, r = {right}, s = {s}, len = {len(s)}")
                result.append(s)
                return
            if left < n:
                print(f"1 *** l = {left}, r = {right}, s = {s}, len = {len(s)}")
                backtrack(s + '(', left + 1, right)
            if right < left:
                print(f"2 *** l = {left}, r = {right}, s = {s}, len = {len(s)}")
                backtrack(s + ')', left, right + 1)
    
        result = []
        backtrack()
        return result
        