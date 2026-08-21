class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] + nums[i] == 0:
                    res.append([nums[i],nums[j], nums[k]])
                    j += 1
                    k = len(nums) - 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                elif (nums[j] + nums[k] + nums[i]) > 0:
                    k -= 1
                else:
                    j += 1
            

        return res


        