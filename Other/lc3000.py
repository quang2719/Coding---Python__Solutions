import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        sq,area = 0.0,0
        for i in range(len(dimensions)):
            l,r = dimensions[i]
            cur = math.sqrt(l**2+r**2)
            if  cur > sq:
                sq = cur
                area = l*r
            elif cur == sq:
                area = max(l*r, area)
        return area