class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        pos = -1
        listofvalue = self.time_map[key]
        left, right = 0, len(listofvalue) - 1
        while left <= right:
            mid = (left + (right - left) // 2)
            if listofvalue[mid][0] <= timestamp:
                pos = mid
                left = mid + 1
            else:
                right = mid - 1
        return listofvalue[pos][1] if pos != -1 else ""
