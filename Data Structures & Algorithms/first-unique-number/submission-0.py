from collections import OrderedDict
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.cnt = Counter(nums)
        self.unique = OrderedDict({i : 1 for i in nums if self.cnt[i] == 1})

    def showFirstUnique(self) -> int:
        if not self.unique:
            return -1
        return next(iter(self.unique.keys()))

    def add(self, value: int) -> None:
        self.cnt[value] += 1
        if self.cnt[value] == 1:
            self.unique[value] = 1
        elif value in self.unique:
            self.unique.pop(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
