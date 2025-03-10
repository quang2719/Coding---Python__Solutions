class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pre = {}
        for i,x in enumerate(nums):
            if x in pre:
                if i - pre[x] <= k: return True
            pre[x] = i
        return False
        
        