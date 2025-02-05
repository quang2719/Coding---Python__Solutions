class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = {}
        self.row = len(grid)
        self.col = len(grid[0])
        for i in range(self.row):
            for j in range(self.col):
                visited[(i,j)] = False

        def getNeighbor(cur):
            i,j = cur
            res = []
            if i-1 >=0:
                res.append((i-1,j))
            if i+1 < self.row:
                res.append((i+1,j))
            if j - 1 >=0:
                res.append((i,j-1))
            if j+1 < self.col:
                res.append((i,j+1))
            return res
            
        def travel(i,j,grid,visited):
            queue = [(i,j)]
            while queue:
                cur = queue.pop()
                visited[cur] = True
                neis = getNeighbor(cur)
                for nei in neis:
                    if not visited[nei] and grid[nei[0]][nei[1]] =='1':
                        queue.append(nei)
            
        
        count = 0
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] =='1' and visited[(i,j)] == False:
                    count +=1
                    travel(i,j,grid,visited)
        return count
