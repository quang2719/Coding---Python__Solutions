import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        count = 0
        for i,x in enumerate(nums):
            heapq.heappush(heap,(x,i))
        for _ in range(k):
            x,i = heapq.heappop(heap)
            x *= multiplier
            nums[i] = x
            heapq.heappush(heap,(x,i))
        return nums