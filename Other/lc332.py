class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        if dp[amount] != amount+1: return dp[amount]
        if len(coins) == 1:
            return int(amount/coins[0]) if amount % coins[0] == 0 else -1

        coins.sort()
        for x in coins: 
            if x > amount: break
            dp[x] = 1
        res = 0
        for i in range(1,amount+1):
            if dp[i] == 1: continue
            
            j = 0
            while j < len(coins) and coins[j] <= i:
                dp[i] = min(dp[i], 1+dp[i-coins[j]])
                j+=1
        if dp[amount] == amount+1:
            return -1
        return dp[amount]
            
        