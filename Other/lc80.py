class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return len(nums)
        left = 2
        while left < len(nums) and not (nums[left] == nums[left-1] and nums[left] == nums[left-2]):
            left+=1
        if left== len(nums): return left
        
        right = left +1
        while right < len(nums):
            nums[left],nums[right] = nums[right],nums[left]
            right +=1
            if not (nums[left] == nums[left-1] and nums[left] == nums[left-2]):
                left +=1
                
        return left
            
            
    
    