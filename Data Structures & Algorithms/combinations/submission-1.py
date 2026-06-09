class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        nums = [x for x in range(1, n + 1)]
        print(f"Nums = {nums}")
        
        def helper(i, curr):
            if len(curr) == k:
                comb.append(curr[:])
                return

            if i >= len(nums):
                return
            
            # Include:
            curr.append(nums[i])
            helper(i + 1, curr)
            curr.pop()

            # Not include
            helper(i + 1, curr)



        helper(0, [])
        return comb
        