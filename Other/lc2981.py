class Solution:
    def maximumLength(self, s: str) -> int:
        dic = {}
        start = 0
        while start < len(s):
            end = start +1
            cur = s[start]
            dic[cur] = dic.get(cur,0)+1
            while end < len(s):
                if s[end] != cur[-1]:
                    break
                else:
                    cur = cur + s[end]
                    dic[cur] = dic.get(cur,0)+1
                    end+=1
            start+=1
        res = -1
        for key,val in dic.items():
            if val >=3:
                res = max(res,len(key))
        return res
        