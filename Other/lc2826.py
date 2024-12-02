class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                count[i] = 1
                continue
            
            val = 1
            for j in range(0,i):
                if nums[i] >= nums[j] and count[j]+1 > val:
                    val = count[j]+1
            count[i] = val
        return len(nums) - max(count)
            