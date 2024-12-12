class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            count = self.bi_search_custom(nums,nums[i]+2*k,i+1,len(nums)-1)
            res = max(res, count-i+1)
        return res
    def bi_search_custom(self, nums, target, left,right):
        while left <= right:
            mid = (left + right)//2
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid -1
        return right
    
        
