class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow = {'a', 'e', 'i', 'o', 'u'}
        dic1 = {}
        dic2 = {}
        for c in s:
            if c in vow:
                dic1[c] = dic1.get(c,0) + 1
            else:
                dic2[c] = dic2.get(c,0) + 1
        best_v = max(dic1.values()) if dic1 else 0
        best_c = max(dic2.values()) if dic2 else 0
        return best_v + best_c
    
                
        
