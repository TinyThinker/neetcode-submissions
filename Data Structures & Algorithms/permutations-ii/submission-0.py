class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        def backtrack(picked, current):
            if len(current) == len(nums):
                results.append(current[:])
                return

            for i in range(len(nums)):
                if i in picked:
                    continue
                
                # <--- CHANGE 2: The Duplicate Check
                # If same as previous, AND previous was not used -> Skip
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in picked:
                    continue

                current.append(nums[i])
                picked.add(i)
                backtrack(picked, current)
                picked.remove(i)
                current.pop()
                


        backtrack(set(), [])
        return results
        