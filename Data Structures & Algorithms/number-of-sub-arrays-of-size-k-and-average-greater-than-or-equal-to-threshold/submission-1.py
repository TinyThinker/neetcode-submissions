class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if not arr or len(arr) < k:
            return 0

        result = 0

        # Initialize window
        curr_sum = 0
        for i in range(k):
            curr_sum += arr[i]

        if (curr_sum / k) >= threshold:
            result += 1
        
        # Iterate the rest of the array       
        for i in range(k, len(arr)):
            curr_sum -= arr[i - k]
            curr_sum += arr[i]
            if (curr_sum / k) >= threshold:
                result += 1

        return result



            



