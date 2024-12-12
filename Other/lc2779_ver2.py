class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        right = 0
        res = 0
        left = 0
        while left < len(nums) and right < len(nums):
            max_val = nums[left] + 2*k
            while right<len(nums) and nums[right] <= max_val: right+=1
            res = max(res, right-left)
            if right < len(nums):
                while nums[right] > nums[left] + 2*k: left+=1
        return res
        
