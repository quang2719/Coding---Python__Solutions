class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        nums.sort()
        wait = 0
        for i,n in enumerate(nums):
            if nums[i] <= 0: wait +=1
            else:
                if nums[i] != i-wait +1:
                    return i - wait+1
        return len(nums) -wait+1