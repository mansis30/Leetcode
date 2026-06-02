class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        ans = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                land_finish = landStartTime[i] + landDuration[i]
                finish1 = max(land_finish, waterStartTime[j]) + waterDuration[j]

                water_finish = waterStartTime[j] + waterDuration[j]
                finish2 = max(water_finish, landStartTime[i]) + landDuration[i]

                ans = min(ans, finish1, finish2)

        return ans