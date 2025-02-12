class Solution(object):
    def check(self,start,end,cumulativeTotal,targetTotal):
        dic_start = cumulativeTotal[start]
        dic_end = cumulativeTotal[end]
        for c in targetTotal.keys():
            s = dic_start.get(c,0)
            e = dic_end.get(c,0) 
            if e == 0: return False
            if e - s < targetTotal[c]: return False
        return True
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t): return ""
        
        target = t
        s = s
        res = ""
        
        targetTotal = {}
        for x in target:
            targetTotal[x] = targetTotal.get(x,0) + 1
        
        cumulativeTotal = [{}]
        for i in range(len(s)):
            cur_ele = cumulativeTotal[i].copy()
            cur_ele[s[i]] = cur_ele.get(s[i],0) + 1
            cumulativeTotal.append(cur_ele)
            
        
        minWindowLen = len(target)
        maxWindowLen = len(s)
        for window in range(minWindowLen,maxWindowLen+1):
            for start in range(0,len(cumulativeTotal) - window):
                end = start + window
                if self.check(
                    start,
                    end,
                    cumulativeTotal,
                    targetTotal
                    ):
                    return s[start:end]
        return ""
            
            
            
s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"
solu = Solution()
print(solu.minWindow(s,t))