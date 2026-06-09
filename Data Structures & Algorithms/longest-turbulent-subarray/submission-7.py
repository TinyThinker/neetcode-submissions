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
                continue
            elif arr[i] > arr[i - 1]: 
                #increasing
                curr_direction = True
            else: 
                curr_direction = False

            cnt, last_direction = self.get_cnt_and_dir(last_direction, curr_direction, cnt)
            res = max(res, cnt)

        return res

    def get_cnt_and_dir(self, last_direction, curr_direction, cnt):
        if last_direction is not None and last_direction ^ curr_direction:
            cnt += 1
        else:
            cnt = 2
        return cnt, curr_direction
