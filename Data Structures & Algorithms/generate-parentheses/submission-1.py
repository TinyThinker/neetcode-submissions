class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []

        def helper(open_count, closed_count ):
            if open_count == n and closed_count == n:
                if temp:
                    res.append("".join(temp))
                return

            # Add opening
            if open_count < n:
                temp.append("(")
                helper(open_count + 1, closed_count)
                temp.pop()


            # Add closing
            if closed_count < open_count:
                temp.append(")")
                helper(open_count, closed_count + 1)
                temp.pop()


        helper(0, 0)
        return res