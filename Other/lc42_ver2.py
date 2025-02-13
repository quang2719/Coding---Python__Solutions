class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left_col = [0 for _ in height]
        max_right_col =[0 for _ in height]
        for i,x in enumerate(height):
            if i > 0:
                max_left_col[i] = max(max_left_col[i-1],x)
            else:
                max_left_col[i] = x
        for i in range(len(height)-1,-1,-1):
            if i < len(height)-1:
                max_right_col[i] = max(max_right_col[i+1],height[i])
            else:
                max_right_col[i] = x
        res = 0
        for i in range(len(height)):
            res += max(0, min(max_left_col[i],max_right_col[i]) - height[i])
        return res