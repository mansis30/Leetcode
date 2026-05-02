class Solution(object):
    def countSubarrays(self, nums, k):
        ans = 0
        j = 0
        mx = deque()
        mn = deque()

        for i in range(len(nums)):
            while mx and nums[mx[-1]] <= nums[i]:
                mx.pop()
            while mn and nums[mn[-1]] >= nums[i]:
                mn.pop()
            mx.append(i)
            mn.append(i)

            while j <= i and (nums[mx[0]] - nums[mn[0]]) * (i - j + 1) > k:
                if mx[0] == j:
                    mx.popleft()
                if mn[0] == j:
                    mn.popleft()
                j += 1
            ans += i - j + 1
        return ans