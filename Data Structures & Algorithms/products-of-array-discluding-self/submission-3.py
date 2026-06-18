class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix product array and a postFix product array.
        # We multiply prefix[i] to get the proudct of all numbers before i
        # and postfix[i] to get the product of all numebers after i.
        # O(N) time complexity and O(N) space complexity if we keep the prefix 
        # and postfix in an array. We could keep it running and have space 
        # complexity of O(1).
        # Example:
        # input = [1, 2, 4, 6]
        # prefix =  [1, 1, 2, 8]
        # postfix = [48, 24 ,6 ,1]
        prefix = [1] * len(nums)
        postfix = prefix[:]
        
        for i in range(1, len(prefix)):
            prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(len(postfix) - 2, -1, -1 ):
            postfix[i] = nums[i+1] * postfix[i+1]


        return [prefix[i] * postfix[i] for i in range(len(nums))]

