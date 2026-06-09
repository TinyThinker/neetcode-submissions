class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr:
            return 0

        last_direction = None
        cnt = 0
        res = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                #no direction
                last_direction = None
                cnt = 1
            elif arr[i] > arr[i - 1]: 
                #increasing
                print(f"i = {i}, Increasing. cnt = {cnt}, last = {last_direction}")
                if last_direction is not None and last_direction ^ True:
                    cnt += 1
                else:
                    cnt = 2
                last_direction = True
            else: 
                #decreasing
                print(f"i = {i}, Decreasing. cnt = {cnt}, last = {last_direction}")
                if last_direction is not None and last_direction ^ False:
                    cnt += 1
                else:
                    cnt = 2
                last_direction = False
            print(f"res={res}, cnt={cnt}")
            res = max(res, cnt)

        return res