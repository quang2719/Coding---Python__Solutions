class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        count = 1
        u,b,l,r = 0, n-1, 0, n -1
        while u<=b and l <= r:
            for col in range(l,r+1):
                res[u][col] = count
                count+=1
            for row in range(u+1,b):
                res[row][r] = count
                count+=1
            
            if u<b:
                for col in range(r,l-1,-1):
                    res[b][col] = count
                    count+=1
                
            if l < r:
                for row in range(b-1,u,-1):
                    res[row][l] = count
                    count+=1
            
            l+=1
            r-=1
            u+=1
            b-=1
        return res