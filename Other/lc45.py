class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jump = [float('inf')] * len(nums)
        min_jump[0] = 0
        for i in range(len(nums)):
            cur_step = min_jump[i]
            for k in range(nums[i]+1):
                if i + k >= len(nums): break
                min_jump[i+k] = min(
                    min_jump[i+k],
                    cur_step + 1
                    )
        return min_jump[len(nums)-1]