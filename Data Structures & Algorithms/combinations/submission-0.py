class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [x for x in range(1, n+1)]
        
        def helper(currState, idx):
            if len(currState) == k:
                res.append(currState[:])
                return
            if idx >= len(nums):
                return

            #include number
            currState.append(nums[idx])
            helper(currState, idx + 1)
            currState.pop()

            # do not include current number
            helper(currState, idx + 1)
            
        helper([], 0)
        return res