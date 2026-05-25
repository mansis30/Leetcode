from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        l = [0] * n
        r = [0] * n

        l[0] = 1
        r[-1] = 1

        
        for i in range(1, n):
            l[i] = nums[i - 1] * l[i - 1]

        
        for i in range(n - 2, -1, -1):
            r[i] = nums[i + 1] * r[i + 1]

       
        op = [0] * n

        for i in range(n):
            op[i] = l[i] * r[i]

        return op
        