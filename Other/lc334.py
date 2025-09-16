class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_left = [0 for x in range(len(nums))]
        max_right = [0 for x in range(len(nums))]
        for i in range(1,len(nums)):
            if i == 1:
                min_left[i] = nums[0]
                continue    
            min_left[i] = min(nums[i-1],min_left[i-1])
        for i in range(len(nums)-2,-1,-1):
            if i == len(nums)-2:
                max_right[i] = nums[i+1]
                continue
            max_right[i] = max(max_right[i+1], nums[i+1])
        
        for i in range(1,len(nums)-1):
            if (
                nums[i] > min_left[i] and
                nums[i] < max_right[i]
            ):
                return True
        return False
            