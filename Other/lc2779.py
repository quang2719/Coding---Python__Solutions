class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        def binary_search(nums, target, left, right):
            """Tìm chỉ số lớn nhất trong nums[left:right+1] nhỏ hơn hoặc bằng target."""
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right  # Trả về chỉ số cuối cùng phù hợp

        nums.sort()  # Sắp xếp danh sách
        res = 0

        for i in range(len(nums)):
            max_index = binary_search(nums, nums[i] + 2 * k, i, len(nums) - 1)
            res = max(res, max_index - i + 1)
        
        return res
