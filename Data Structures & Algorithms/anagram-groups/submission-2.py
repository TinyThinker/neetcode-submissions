from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Let's sort all of the words and add them to a dictionary.
        d = defaultdict(list)
        for s in strs:
            tmp = "".join(sorted(s))
            d[tmp].append(s)
        return list(d.values())

        