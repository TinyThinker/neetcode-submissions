class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def helper(i):
            if i <= 1:
                return 0

            if i in memo:
                return memo[i]

            current = 0
            if i < len(cost):
                current = cost[i]

            cost_to_reach_from_one_step = helper(i - 1) + cost[i - 1]
            cost_to_reach_from_two_steps = helper(i - 2) + cost[i - 2]
            memo[i] = min(cost_to_reach_from_one_step, cost_to_reach_from_two_steps)
            return memo[i]
        return helper(len(cost))

        