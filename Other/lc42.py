class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_len = 0
        candidate = []
        
        for col,hei in enumerate(height):
            max_len = max(max_len,hei)
            candidate.append((hei,col))
        water_row = 1
        res = 0
        while water_row <= max_len:
            pre = -1
            remList = []
            for hei,col in candidate:
                if hei >= water_row:
                    if pre == -1:
                        pre = col
                    else:
                        if col - pre > 1:
                            res += col - pre -1
                        pre = col
                else:
                    remList.append((hei,col))
            for pair in remList:
                candidate.remove(pair)
            water_row +=1
        return res