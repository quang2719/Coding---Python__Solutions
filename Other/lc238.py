class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count0 = 0
        alt = 0
        product = 1
        for i,x in enumerate(nums):
            if x == 0:
                count0 +=1
                alt = i
            else:
                product *= x
        res = []
        if count0 >=2:
            return [0 for _ in nums]
        elif count0 == 1:
            return [(product if i == alt else 0) for i in range(len(nums))]
        else:        
            for x in nums:
                res.append(product/x)
            return res