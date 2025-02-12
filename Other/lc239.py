class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums): return [max(nums)]
        if k == 1: return nums
        
        res = []
        cur_max = nums[0]
        window = {}
        for x in nums[:k]:
            window[x] = window.get(x,0)+1
            cur_max = max(cur_max,x)
        res.append(cur_max)
        
        for i in range(1,len(nums)-k+1):
            old = nums[i-1]
            new = nums[i+k-1]
            window[new] = window.get(new,0)+1
            window[old] -=1
            check = False
            if window[old] == 0:
                window.pop(old)
                check = True
            if new >= cur_max: 
                cur_max = new
                res.append(cur_max)
                continue
            elif cur_max == old and check:
                 cur_max = max(window.keys())
            res.append(cur_max)
            
        return res