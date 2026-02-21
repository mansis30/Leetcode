class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        temp=sorted(nums)
        if temp[-1]>=2*temp[-2]:
            for i in range(len(nums)):
                if nums[i]==temp[-1]:
                    return i
        return -1