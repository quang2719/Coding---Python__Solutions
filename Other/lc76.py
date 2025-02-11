class Solution(object):
    def check(start,end,cumulativeTotal,targetTotal):
        res = True
        dic_start = cumulativeTotal[start]
        dic_end = cumulativeTotal[end]
        for c in targetTotal.keys():
            s = dic_start.get(c,0)
            e = dic_end.get(c,0) 
            if e == 0: return False
            if e - s != targetTotal[c]: return False
        return True
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t): return ""
        
        target = t.split()
        s = s.split()
        res = ""
        
        targetTotal = {}
        for x in target:
            num = ord(x)
            targetTotal[num] = targetTotal.get(num,0) + 1
        
        cumulativeTotal = [{}]
        for i in range(len(s)):
            added_num = ord(s[i])
            cur_ele = cumulativeTotal[i].copy()
            cur_ele[added_num] = cur_ele.get(added_num,0) + 1
            cumulativeTotal.append(cur_ele)
        
        minWindowLen = len(target)
        maxWindowLen = len(s)
        for window in range(minWindowLen,maxWindowLen+1):
            for start in range(0,len(cumulativeTotal) - window):
                end = start + window
                # check end - start
                if self.check(start,end,cumulativeTotal,targetTotal):
                    return s[start:end+1]
        return False
            
            
            
s ="ADOBECODEBANC"
t = "ABC"
solu = Solution()
print(solu.minWindow(s,t))