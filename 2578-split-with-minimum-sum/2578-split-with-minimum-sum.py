class Solution:
    def splitNum(self, num: int) -> int:
        num=list(str(num))
        num.sort()
        n1=""
        n2=""
        for i in range(len(num)):
            if i%2==0:
                n1+=num[i]
            else:
                n2+=num[i]
        return int(n1)+int(n2)