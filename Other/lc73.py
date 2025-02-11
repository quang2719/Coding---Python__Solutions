class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        remRow = {}
        remCol = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    remRow[row] = True
                    remCol[col] = True
        
        for row in remRow.keys():
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        for col in remCol.keys():
            for row in range(len(matrix)):
                matrix[row][col] = 0
        
            
        