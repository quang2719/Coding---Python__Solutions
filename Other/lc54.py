class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        u,b,l,r = 0,len(matrix)-1,0, len(matrix[0])-1
        res = []
        while l<=r and u<= b:
            if l<=r:
                for col in range(l,r+1):
                    res.append(matrix[u][col])

            for row in range(u+1,b):
                res.append(matrix[row][r])

            if l<=r and u < b:
                for col in range(r,l-1,-1): 
                    res.append(matrix[b][col])
            if l<r:
                for row in range(b-1, u, -1):
                    res.append(matrix[row][l])
            l+=1
            r-=1
            u+=1
            b-=1
        return res
        
            
        