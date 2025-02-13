class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        pre = []
        for i in range(len(s)):
            if s[:i+1]in wordDict:
                pre.append(i)
                continue
            for p in pre:
                if s[p:i+1] in wordDict:
                    pre.append(i)
                    break
        print(pre)
        return len(s) == pre[-1]