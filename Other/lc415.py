class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def addBigNum (num1,num2):
            if len(num1) > len(num2): return addBigNum(num2,num1)
            if len(num1) < 4 and len(num2) <4: return str(int(num1) + int(num2))

            num1 = ''.join(['0' for _ in range(len(num2)-len(num1))]) + num1
            res = [0] * (len(num2) +1)

            r = len(num2)-1
            plus = 0
            while r>=0:
                cur = int(num1[r]) + int(num2[r]) + plus
                if cur > 9:
                    plus = 1
                    cur = cur %10
                    res[r+1] = cur
                else:
                    plus = 0
                    res[r+1] = cur
                r-=1
            if plus:
                res[0] = plus
                return ''.join([str(x) for x in res])
            else:
                return ''.join([str(x) for x in res[1:]])
        return addBigNum(num1,num2)
