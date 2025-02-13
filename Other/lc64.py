class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for _ in grid[0]] for _ in grid]
        # fill first row
        for col in range(len(grid[0])):
            dp[0][col] = (
                        grid[0][col] if col == 0 else 
                        dp[0][col-1] + grid[0][col]
                        )
        # fill first col
        for row in range(1,len(grid)):
            dp[row][0] = dp[row-1][0] + grid[row][0]
            
        for row in range(1,len(grid)):
            for col in range(1,len(grid[0])):
                dp[row][col] = (grid[row][col] + 
                                min(dp[row][col-1],dp[row-1][col]))
        return dp[len(grid)-1][len(grid[0])-1]
    
solu = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(solu.minPathSum(grid))