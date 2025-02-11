class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        mark = {}
        for r in matrix:
            for e in r:
                mark[e] = True
        return mark.get(target,False)