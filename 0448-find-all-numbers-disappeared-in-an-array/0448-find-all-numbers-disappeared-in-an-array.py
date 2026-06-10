class Solution:
    def findDisappearedNumbers(self, nums):
        nums.sort()
        return [i for i in range(1, len(nums)+1) if nums[bisect_left(nums, i)%len(nums)] != i]