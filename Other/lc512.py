class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 0
        cur_range = (0,0)
        for left,right in points:
            if cur_range == (0,0):
                cur_range = (left,right)
                continue
            _,pre_right = cur_range
            if left > pre_right:
                res +=1
                cur_range = (left,right)
            else:
                cur_range = (
                    left,
                    min(right,pre_right)
                )
        return res
                