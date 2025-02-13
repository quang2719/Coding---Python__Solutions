class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i,x in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                return nums[i]