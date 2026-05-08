class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        prefix = [0] * len(nums)
        curr = 0
        for i in range(0, len(nums)):
            prefix[i] = curr
            curr += nums[i]
        idx = -1
        curr = 0
        for i in range(len(nums) - 1, -1, -1):
            if curr == prefix[i]:
                idx = i
            curr += nums[i]
        return idx