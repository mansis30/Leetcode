class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=0
        k=len(nums)
        for i in range(0,k-1,2):
           n+=min(nums[i],nums[i+1])
        return n
        