class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 1:
            min_i = len(nums)-2
            while min_i >= 0 and nums[min_i] >= nums[min_i+1]:
                min_i-=1
            if min_i < 0:
                nums[:] = nums[::-1]
            else:
                j = len(nums)-1
                while j>min_i and nums[j] <= nums[min_i]:
                    j-=1
                nums[min_i], nums[j] = nums[j],nums[min_i]
                nums[min_i + 1:] = reversed(nums[min_i+ 1:]) 
                
                
            
            

        
            
        