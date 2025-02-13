class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p): return []
        
        pDic = {}
        for x in p:
            pDic[x]  = pDic.get(x,0)+1
        sDic = [{}]
        res = []
        for i in range(0,len(s)+1):
            if i == 0: continue
            
            # handle s[i-1]
            curDic = sDic[i-1].copy()
            curDic[s[i-1]] = curDic.get(s[i-1],0) + 1
            sDic.append(curDic)
            
            # check sliding window
            if i >= len(p):
                check = True
                for x in pDic.keys():
                    end = sDic[i].get(x,0)
                    if end == 0: 
                        check = False
                        break
                    start = sDic[i-len(p)].get(x,0)
                    if end - start != pDic[x]:
                        check = False
                        break
                if check:
                    res.append(i-len(p))
        return res        