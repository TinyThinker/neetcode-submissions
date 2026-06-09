class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        memo = [1, 2]
        result = None
        for i in range(2, n):
            result = memo[-1] + memo[-2]
            memo[-1], memo[-2] = result, memo[-1]

        return result


        # def helper(n):
        #     if n <= 2:
        #         return n

        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        # return helper(n)

        