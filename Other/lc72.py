class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        dp = [
            [-1 for _ in range(len(word2)+1)] 
            for _ in range(len(word1)+1)
            ]
        dp[0][0] = 0 # from empty to empty
        # fill first row
        for j in range(1,len(word2)+1):
            dp[0][j] = j # insert cost
        for i in range(1,len(word1)+1):
            dp[i][0] = i # delete cost
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                # dp i,j contain cost from word1[:i] to word2[:j]
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    continue  
                dp[i][j] = 1 + min(
                    dp[i-1][j-1], # replace cost
                    dp[i-1][j], # delete
                    dp[i][j-1] # insert  
                ) 
        return dp[len(word1)][len(word2)]