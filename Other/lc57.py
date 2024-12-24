class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        id = self.custom_bisearch(intervals, newInterval[0])
        intervals.insert(id, newInterval)
        if id > 0:
            self.handle_overlap(intervals, id - 1)
        if id < len(intervals) - 1:
            self.handle_overlap(intervals, id)
        return intervals

    def handle_overlap(self, nums, id):
        while id < len(nums) - 1 and nums[id][1] >= nums[id + 1][0]:
            nums[id][1] = max(nums[id + 1][1],nums[id][1])
            nums[:] = nums[: id + 1] + (
                nums[id + 2 :] if id + 2 < len(nums) else []
                )

    def custom_bisearch(self, nums, i_start):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid][0] < i_start:
                left = mid + 1
            else:
                right = mid
        return left
