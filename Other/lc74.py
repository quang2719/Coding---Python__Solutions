class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def biSearchRow(target,matrix):
            left = 0
            right = len(matrix)-1
            if target >= matrix[right][0]:
                return right
            while left <= right:
                mid = (left+right)//2
                if matrix[mid][0] <= target:
                    if target < matrix[mid+1][0]:
                        return mid
                    else:
                        left = mid+1
                else:
                    right = mid -1
            return -1
        def biSearchCol(target,matrix,row):
            if row == len(matrix)-1 and matrix[-1][-1] < target:
                return False
            left = 0
            right = len(matrix[row]) -1
            while left <= right:
                mid = (left+right)//2
                if matrix[row][mid] == target: return True
                elif matrix[row][mid] < target:
                    left = mid+1
                else:
                    right = mid -1
            return False
        
        row = biSearchRow(target,matrix)
        if matrix[row][0] == target:
            return True
        if row == -1: return False
        return biSearchCol(target,matrix,row)
                


