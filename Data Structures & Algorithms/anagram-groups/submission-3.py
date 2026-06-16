from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Let's sort all of the words and add them to a dictionary.
        # m * n log n, n
        # d = defaultdict(list)
        # for s in strs:
        #     tmp = "".join(sorted(s))
        #     d[tmp].append(s)
        # return list(d.values())
        
        # We can cound the characters and represent as a touple of the array
        d = {}
        for s in strs:
            freq = [0]* 26
            for c in s:
                freq[ord(c.lower()) - ord('a')] += 1
            if tuple(freq) in d:
                d[tuple(freq)].append(s)
            else:
                d[tuple(freq)] = [s]

        return list(d.values())

            



        