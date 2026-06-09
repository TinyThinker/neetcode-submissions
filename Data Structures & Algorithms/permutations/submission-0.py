class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(picked, current):
            if len(current) == len(nums):
                results.append(current[:])
                return

            for i in range(len(nums)):
                if i in picked:
                    continue

                current.append(nums[i])
                picked.add(i)
                backtrack(picked, current)
                picked.remove(i)
                current.pop()
                


        backtrack(set(), [])
        return results


        