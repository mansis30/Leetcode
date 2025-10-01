class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[0]*(len(triangle)+1)
        triangle.reverse()
        for row in triangle:
            for i,val in enumerate(row):
                dp[i]=min(dp[i],dp[i+1])+val
        return dp[0]