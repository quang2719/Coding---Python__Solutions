class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums): return 0
        max_len = 1
        len_sub_arr = []
        while max_len <= len(nums):
            if max_len == 1:
                for num in nums:
                    if num >= target: return max_len
                    len_sub_arr.append(num)
            else:
                for i in range(max_len-1,len(nums)):
                    len_sub_arr[i] += nums[i - max_len+1]
                    if len_sub_arr[i] >= target:
                        return max_len
            max_len+=1
        return 0