class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        left = 0
        while left < len(nums):
            right = left +1
            while right < len(nums) and nums[right] == nums[right-1]+1:
                right +=1
            
            if left + 1 != right:
                res.append(f"{nums[left]}->{nums[right - 1]}")
            else:
                res.append(f"{nums[left]}")
            left = right
        return res