class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums
        
        res = []
        i = 0
        while i < len(nums)-1:
            if nums[i]!=0:
                if nums[i]== nums[i+1]:
                    res.append(2*nums[i])
                    i+=1
                else:
                    res.append(nums[i])
            i+=1
        if i == len(nums)-1:
            res.append(nums[i])
        while len(res) < len(nums): res.append(0)
        return res
             