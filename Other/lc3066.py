import heapq
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i,x in enumerate(nums):
            heapq.heappush(heap,(x,i))
        count = 0
        id = len(nums)
        while len(heap) >= 2:
            x,i = heapq.heappop(heap)
            if x>=k: break
            y,i = heapq.heappop(heap)
            heapq.heappush(heap,( x * 2 +  y,id))
            id+=1
            count+=1
        return count
solul = Solution()
nums = [2,11,10,1,3]
k = 10
print(solul.minOperations(nums,k))
        
            