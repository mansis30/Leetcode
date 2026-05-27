class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        N = len(machines)
        total_sum = sum(machines)
        avg = total_sum // N

        if total_sum % N != 0:
            return -1

        imbalances = [machines[i] - avg for i in range(N)]

        res = float('-inf')
        D_i = 0
        for i in range(N):
            res = max(res, abs(D_i))
            res = max(res, imbalances[i])
            D_i += imbalances[i]
        
        return res