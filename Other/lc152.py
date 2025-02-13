class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_pre = []
        min_pre = []
        res = nums[0]
        for i,x in enumerate(nums):
            if i == 0:
                res = max(res,x)
                max_pre.append(x)
                min_pre.append(x)
            else:
                cur_max = max(
                    max_pre[-1]*x,
                    min_pre[-1]*x,
                    x)
                cur_min = min(
                    max_pre[-1]*x,
                    min_pre[-1]*x,
                    x)
                res = max(res,cur_max)
                max_pre.append(cur_max)
                min_pre.append(cur_min)
        return res
                