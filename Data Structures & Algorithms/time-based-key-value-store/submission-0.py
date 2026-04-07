class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            arr = self.store[key]
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid][1] == timestamp:
                    return arr[mid][0]
                if timestamp < arr[mid][1]:
                    r = mid - 1
                else:
                    l = mid + 1

            return arr[0][0]
        else:
            return None
