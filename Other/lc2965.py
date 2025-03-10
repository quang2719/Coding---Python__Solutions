class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        arr = [x for x in range(1,n*n+1)]
        dup = 0
        for rows in grid:
            for x in rows:
                if x in arr:
                    arr.pop(x)
                else: dup = x
        return [dup,arr.pop()]