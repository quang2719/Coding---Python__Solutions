class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ar = [x for x in set(nums)]
        ar.sort()
        i = 0
        res = 0
        while i < len(ar)-1:
            tmp = 1
            while i < len(ar)-1 and ar[i] == ar[i+1]-1 :
                tmp+=1
                i+=1
            res = max(res,tmp)
            i +=1
        return res
        