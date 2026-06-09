class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol, res = [], []
        
        def backtracking(i):
            if i == len(nums):
                res.append(sol[:])
                return
            
            # Do not use number:
            backtracking(i+1)

            # Do use number
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()


        backtracking(0)
        return res