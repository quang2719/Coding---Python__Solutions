class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(nums, target, l ,r):
            if l >r: return -1
            mid = (l+r)//2
            if nums[mid] == target: return mid
            elif nums[mid] < target:
                return search(nums,target, mid+1,r)
            else:
                return search(nums, target, l, mid-1)
        
        id = search(nums, target, 0, len(nums)-1)
        if id == -1: return [-1,-1]

        start,end = id,id
        while start >0 and nums[start-1] == target:
            start-=1
        while end < len(nums)-1 and nums[end+1] == target:
            end+=1
        return [start,end]
            