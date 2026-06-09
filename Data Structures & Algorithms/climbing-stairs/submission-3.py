class Solution:
    def climbStairs(self, n: int) -> int:
        tab = [1, 1]

        for i in range(2, n + 1):
            tab.append(tab[i-2] + tab[i-1])
            #result = self.climbStairs(n-1) + self.climbStairs(n-2)
        return tab[n]
        