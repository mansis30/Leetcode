class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        return self.heapSort(nums)
    def heapSort(self, arr):
        n = len(arr)
        heapq.heapify(arr)
        res = [0 for _ in range(n)]
        for i in range(n):
            minn = heapq.heappop(arr)
            if not i%2:
                res[i+1] = minn
            else:
                res[i-1] = minn
        return res
        