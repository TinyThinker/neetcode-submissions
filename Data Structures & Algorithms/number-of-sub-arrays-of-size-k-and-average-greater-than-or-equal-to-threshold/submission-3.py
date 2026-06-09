class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if not arr or len(arr) < k:
            return 0

        result = 0

        l = 0
        curr_sum = 0
        for r in range(len(arr)):
            curr_sum += arr[r]

            if (r - l + 1) == k:
                if curr_sum / k >= threshold:
                    result += 1
                curr_sum -= arr[l]
                l += 1


        return result



            



