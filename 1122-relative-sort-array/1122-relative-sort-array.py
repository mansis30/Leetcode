class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2dict = {}
        i = 0
        for x in arr2:
            arr2dict[x] = i
            i += 1
        extras = []
        available = []
        for x in arr1:
            if x not in arr2dict:
                extras.append(x)
            else:
                available.append(x)
        available.sort(key = lambda x: arr2dict[x])
        extras.sort()
        return available+extras