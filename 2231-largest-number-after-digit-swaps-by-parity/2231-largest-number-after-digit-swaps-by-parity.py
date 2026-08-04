class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(d) for d in str(num)]

        odd = sorted([d for d in digits if d % 2 == 1],reverse=True)
        even = sorted([d for d in digits if d % 2 == 0],reverse=True)

        res = []
        odd_idx,even_idx = 0,0

        for d in digits:
            if d % 2 == 1:
                res.append(odd[odd_idx])
                odd_idx += 1
            else:
                res.append(even[even_idx])
                even_idx += 1

        return int(''.join(map(str,res)))
        