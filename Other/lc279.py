class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        candi = {}
        dp = [0 for _ in range(n+1)]
        while i*i < n:
            dp[i*i] = 1
            i+=1
        if i*i == n: return 1
        
        for i in range(2,n+1):
            if dp[i] == 0:
                dp[i] = float('inf')
                j = 1
                while j*j < i:
                    dp[i] = min(dp[i],1 + dp[i-j*j])
                    j+=1
        return dp[n]
        
        
        
        
        