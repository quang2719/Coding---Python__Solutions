from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums): return 0
        # binary search idea
        left = 1
        right = len(nums)
        while left <= right:
            mid = (left+right)//2
            if self.max_of_wind(target,nums,mid): # windows len mid >= target
                right = mid - 1
            else:
                left = mid + 1
        return left
    def max_of_wind(self, target: int, nums:List, win_len: int):
        win_sum = 0
        for i in range(win_len):
            win_sum += nums[i]
        if win_sum >= target: return True
        for i in range(win_len,len(nums)):
            win_sum -=  nums[i-win_len]
            win_sum += nums[i]
            if win_sum >= target: return True
        return False