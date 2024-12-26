from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jump = [1001] * len(nums)
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

# Tạo một trường hợp kiểm thử tùy chỉnh
solution = Solution()

# Trường hợp kiểm thử 1
nums = [2, 3, 1, 1, 4]
print(solution.jump(nums))  # Output: 2 (Nhảy từ 2 -> 3 -> 4)

# Trường hợp kiểm thử 2
nums = [2, 3, 0, 1, 4]
print(solution.jump(nums))  # Output: 2 (Nhảy từ 2 -> 3 -> 4)

# Trường hợp kiểm thử 3
nums = [1, 2, 3]
print(solution.jump(nums))  # Output: 2 (Nhảy từ 1 -> 2 -> 3)

# Trường hợp kiểm thử 4
nums = [1, 1, 1, 1]
print(solution.jump(nums))  # Output: 3 (Nhảy từ 1 -> 1 -> 1 -> 1)

# Trường hợp kiểm thử 5
nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
print(solution.jump(nums))  # Output: 1 (Nhảy từ 10 -> 0)