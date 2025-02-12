class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_digit = {}
        res = -1
        for x in nums:
            cur = 0
            tmp = x
            while tmp >0:
                cur += tmp%10
                tmp//=10
            if cur in total_digit.keys():
                total_digit[cur].append(x)
            else:
                total_digit[cur] = [x]
        for pair in total_digit.values:
            if len(pair) < 2:
                continue
            max1 = pair[0]
            max2 = max1
            for x in pair:
                if x > max1:
                    max2 = max1
                    max1 = x
                elif x > max2:
                    max2 = x
            res = max(res,max1+max2)
        return res