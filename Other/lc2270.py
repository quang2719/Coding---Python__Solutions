class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum =0
        count = 0
        for i in range(len(nums)-1):
            left_sum += nums[i]
            if left_sum >= (total - left_sum):
                count+=1
        return count