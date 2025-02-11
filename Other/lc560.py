from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return min(nums)
        q = PriorityQueue(k+1)
        for i,x in enumerate(nums):
            if q.full():
                q.get()
            q.put((x,i))
        q.get()
        x,i = q.get()
        return x