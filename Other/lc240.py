class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nOfRow = len(matrix)
        nOfCol = len(matrix[0])
        # find row
        left = 0
        right = nOfRow-1
        while True:
            if left >= right:
                break
            mid = (left + right) //2
            if target <= matrix[mid][0]:
                right = mid-1
            else:
                left = mid+1
        row = right
        
        # find column
        left = 0
        right = nOfCol-1
        while True:
            if left >= right:
                break
            mid = (left + right) //2
            if target <= matrix[row][mid]:
                right = mid-1
            else:
                left = mid+1
        col = right
        return target == matrix[row][col]
                
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
solu = Solution()
print(solu.searchMatrix(matrix,target))