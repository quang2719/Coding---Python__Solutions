class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows: return s
        if len(s) ==1 or numRows ==1: return s
        dic = {i:[] for i in range(numRows)}
        res = ""
        for i in range(len(s)):
            tmp = i % (2*(numRows-1))
            if tmp < numRows:
                dic[tmp].append(s[i])
            else: dic[2*(numRows-1) -tmp].append(s[i])
        for i in range(numRows):
            for x in dic[i]: res += x
        return res

        