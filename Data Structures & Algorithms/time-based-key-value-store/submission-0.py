class TimeMap:

    def __init__(self):
        self.key_value = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_value:
            return ""
        arr = self.key_value[key]


        l, r = 0, len(arr) - 1

        res = -1
        while l <= r:
            mid = l + (r-l)//2
            curr_time = arr[mid][1]
            if  curr_time <= timestamp:
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        
        return "" if res == -1 else arr[res][0]