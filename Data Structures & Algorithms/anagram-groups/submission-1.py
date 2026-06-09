class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We are given an array of strings "words".
        # We need to group these words if they are anagram.
        # How can we group them?
        # We can use a HashMap where the key indicates the footprint of anagrams
        # and the value is a list of all of the strings who share that footprint.
        res = defaultdict(list)
        
        for s in strs:
            res["".join(sorted(s))].append(s)
            # footprint = [0] * 26
            # for c in s:
            #     i = ord(c) - ord('a')
            #     footprint[i] += 1
            # res[tuple(footprint)].append(s)

        
        return list(res.values())

        # res = defaultdict(list)

        # for s in strs:
        #     res["".join(sorted(s))].append(s)

        # return list(res.values())
