class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for n in nums:
            self.prefix.append(n + self.prefix[-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]