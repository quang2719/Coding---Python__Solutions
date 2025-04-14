class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        if len(nums)<3: return 0
        
        max_ij = [0]
        pre_i = nums[0]
        for j in range(1,len(nums)):
            max_ij.append(pre_i-nums[j])
            pre_i = max(pre_i,nums[j])
        res = -float('inf')
        pre_ij = max_ij[1]
        for k in range(2,len(nums)):
            res = max(res, nums[k]*pre_ij)
            pre_ij = max(pre_ij,max_ij[k])
        if res <= 0: return 0
        return res