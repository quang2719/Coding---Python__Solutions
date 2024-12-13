class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        if n ==1: return s
        res = s[0]
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = True
            if i < n-1 and s[i]==s[i+1]:
                dp[i][i+1] = True
                res = s[i:i+2]
        for step in range(2,n):
            for i in range(0,n-step):
                if s[i] == s[i+step] and dp[i+1][i+step-1]:
                    dp[i][i+step] = True
                    res = s[i:i+step+1]
        return res
        
                                                                                                                                                                 
        


        