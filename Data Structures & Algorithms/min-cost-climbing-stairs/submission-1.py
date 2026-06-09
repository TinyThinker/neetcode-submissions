class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def helper(i):
            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            current = 0
            if i < len(cost):
                current = cost[i]

            memo[i] = min(helper(i-1), helper(i-2)) + current
            return memo[i]
        return helper(len(cost))

        