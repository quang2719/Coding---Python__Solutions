class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        def isPreSuf(s1,s2):
            if len(s1)>len(s2): return False
            l = len(s1)
            return s2.startswith(s1) and s2.endswith(s1)
        for i in range(len(words)-1):
            j = i+1
            while j < len(words):
                if isPreSuf(words[i],words[j]): count+=1
                j+=1
        return count
