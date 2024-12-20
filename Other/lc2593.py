import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return min(nums)
        heap = []
        res = 0
        checked = [False] * len(nums)
        for i,x in enumerate(nums):  
            heapq.heappush(heap, (x,i))

        while heap:
            val,id = heapq.heappop(heap)
            if not checked[id]:
                res += val
                if id == 0:
                    checked[id+1] = True
                elif id == len(nums)-1: checked[id-1] = True
                else: 
                    checked[id-1] = True 
                    checked[id+1] = True
        return res