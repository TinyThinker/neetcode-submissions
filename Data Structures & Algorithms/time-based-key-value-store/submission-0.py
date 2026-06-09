class TimeMap:

    def __init__(self):
        self.kv_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv_map:
            self.kv_map[key] = []
        self.kv_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.kv_map.get(key, [])
        res = ""
        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r - l) // 2
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] < timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res



        
