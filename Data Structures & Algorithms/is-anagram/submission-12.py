class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # We could sort the strings and make sure that they are the same.
        # This would be an O(n log n) time complexity 
        # While having an O(1) space complexity.
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

        # Alterntively we could create a fequency dictionary of characters in both strings.
        # if they are the same then we are good
        # Time complexity O(N)
        # Space complexity O(n)