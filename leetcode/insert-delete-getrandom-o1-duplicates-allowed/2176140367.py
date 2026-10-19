class RandomizedCollection:

    def __init__(self):
        self.d = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        not_present = val not in self.d
        if not_present:
            self.d[val] = set()
        self.d[val].add(len(self.nums))
        self.nums.append(val)
        return not_present

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        idx = self.d[val].pop()
        last = self.nums[-1]
        last_idx = len(self.nums) - 1
        if idx != last_idx:
            self.nums[idx] = last
            self.d[last].remove(last_idx)
            self.d[last].add(idx)
        self.nums.pop()
        if not self.d[val]:
            del self.d[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()